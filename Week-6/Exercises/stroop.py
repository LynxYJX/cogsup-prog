from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_j, K_f, K_SPACE
import random

""" Constants """
KEYS = [K_j, K_f]
TRIAL_TYPES = ['match', 'mismatch']
COLORS = ['red','blue','green','orange']

N_BLOCKS = 2
N_TRIALS_IN_BLOCK = 16

INSTR_START = """
In this task, you have to indicate whether the meaning of a word and the color of its font match.

Press J if they do.
Press F if they do not.

Press SPACE to begin.
"""
INSTR_MID = """You have finished half of the experiment, well done! Your task will be the same.\n\nTake a break, then press SPACE to move on to the second half."""

FEEDBACK_CORRECT = """Correct"""
FEEDBACK_INCORRECT = """Incorrect"""

""" Helper functions """
def load(stims):
    for stim in stims:
        stim.preload()

def present_for(stim, t=1000):
    stim.present()
    exp.clock.wait(t)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait(K_SPACE)

""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_id', 'trial_id', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode(True)
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} for w in COLORS}
load([stims[w][c] for w in COLORS for c in COLORS])

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT, text_colour='green')
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT, text_colour='red')
load([feedback_correct, feedback_incorrect])

# Create a list to store results for final calculation
results = []

""" Experiment """
def run_trial(block_id, trial_id, trial_type, word, color):
    stim = stims[word][color]
    present_for(fixation, t=500)
    stim.present()
    key, rt = exp.keyboard.wait(keys=KEYS)
    
    correct_response = (trial_type == "match" and key == K_j) or \
                       (trial_type == "mismatch" and key == K_f)
    
    # Add data to expyriment's file
    exp.data.add([block_id, trial_id, trial_type, word, color, rt, correct_response])
    # add the boolean result to list
    results.append(correct_response)
    
    feedback = feedback_correct if correct_response else feedback_incorrect
    present_for(feedback, t=1000)

control.start()

present_instructions(INSTR_START)
for block_id in range(1, N_BLOCKS + 1):
    for trial_id in range(1, N_TRIALS_IN_BLOCK + 1):
        trial_type = random.choice(TRIAL_TYPES)
        word = random.choice(COLORS)
        
        if trial_type == 'match':
            color = word
        else:
            possible_colors = [c for c in COLORS if c != word]
            color = random.choice(possible_colors)
            
        run_trial(block_id, trial_id, trial_type, word, color)
        
    if block_id != N_BLOCKS:
        present_instructions(INSTR_MID)
        
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
