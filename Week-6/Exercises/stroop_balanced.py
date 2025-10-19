import random
import itertools
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_r, K_b, K_g, K_o, K_SPACE

""" Constants """
COLORS = ['red', 'blue', 'green', 'orange']
KEY_MAP = {'red': K_r, 'blue': K_b, 'green': K_g, 'orange': K_o}
KEYS = list(KEY_MAP.values())

N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 16

# Updated instructions 
INSTR_START = """
In this task, you have to indicate the FONT COLOR of the word you see.

Press R for RED
Press B for BLUE
Press G for GREEN
Press O for ORANGE

Ignore the meaning of the word. Please respond as quickly and accurately as possible.

Press SPACE to begin.
"""
INSTR_MID_TEMPLATE = """You have finished block {block_done} of {total_blocks}. Well done!

Take a short break, then press SPACE to continue."""

FEEDBACK_CORRECT = """Correct"""
FEEDBACK_INCORRECT = """Incorrect"""

""" Helper functions """
def derangements(lst):
    """Generates all derangements of a list, where no element is in its original position."""
    ders = []
    for perm in itertools.permutations(lst):
        if all(original != perm[idx] for idx, original in enumerate(lst)):
            ders.append(perm)
    return ders

def present_for(stim, t=1000):
    stim.present()
    exp.clock.wait(t)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait(K_SPACE)

""" Global settings """
exp = design.Experiment(name="Balanced Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_id', 'trial_id', 'trial_type', 'word', 'color', 
                             'correct_key', 'pressed_key', 'RT', 'correct'])

control.set_develop_mode(True)
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} for w in COLORS}
feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT, text_colour='green')
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT, text_colour='red')

# Preload all stimuli
fixation.preload()
for w in COLORS:
    for c in COLORS:
        stims[w][c].preload()
feedback_correct.preload()
feedback_incorrect.preload()

# Create a list to store results for final calculation
results = []

""" Experiment Trial Function """
def run_trial(block_id, trial_id, trial_info):
    word = trial_info['word']
    color = trial_info['color']
    trial_type = "match" if word == color else "mismatch"
    correct_key = KEY_MAP[color]
    
    stim = stims[word][color]
    present_for(fixation, t=500)
    stim.present()
    
    key, rt = exp.keyboard.wait(keys=KEYS)
    correct_response = (key == correct_key)
    
    exp.data.add([block_id, trial_id, trial_type, word, color, 
                  correct_key, key, rt, correct_response])
    results.append(correct_response)
    
    feedback = feedback_correct if correct_response else feedback_incorrect
    present_for(feedback, t=1000)

""" Main Experiment """
control.start()

subject_id = exp.subject
ALL_DERANGEMENTS = derangements(COLORS)
perm_index = (subject_id - 1) % len(ALL_DERANGEMENTS)
mismatch_permutation = ALL_DERANGEMENTS[perm_index]

base_trials = []
base_trials.extend([{"word": c, "color": c} for c in COLORS]) # 4 match trials
base_trials.extend([{"word": w, "color": c} for w, c in zip(COLORS, mismatch_permutation)]) # 4 mismatch trials

all_blocks = []
block_repetitions = N_TRIALS_IN_BLOCK // len(base_trials) 
for _ in range(N_BLOCKS):
    current_block_trials = base_trials * block_repetitions
    random.shuffle(current_block_trials)
    all_blocks.append(current_block_trials)


present_instructions(INSTR_START)

for block_idx, block_trials in enumerate(all_blocks, 1):
    for trial_idx, trial in enumerate(block_trials, 1):
        run_trial(block_id=block_idx, trial_id=trial_idx, trial_info=trial)
    
    if block_idx != N_BLOCKS:
        instr_mid = INSTR_MID_TEMPLATE.format(block_done=block_idx, total_blocks=N_BLOCKS)
        present_instructions(instr_mid)

# Accuracy feedback (in %)
total_trials = len(results)
# sum() on a list of booleans works because True=1 and False=0
correct_trials = sum(results)

accuracy = 0.0
if total_trials > 0:
    accuracy = (correct_trials / total_trials) * 100

feedback_text = f"You have finished the experiment!\n\nYour final accuracy was: {accuracy:.1f}%\n\nPress SPACE to quit."
final_screen = stimuli.TextScreen("Results", feedback_text)
final_screen.present()
exp.keyboard.wait(K_SPACE)

control.end()
