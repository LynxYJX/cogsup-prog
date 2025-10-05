import expyriment
from expyriment.misc.constants import K_SPACE
from expyriment import design, control, stimuli

# 1: Global Settings 

exp = design.Experiment(name="Ternus Illusion")
control.set_develop_mode()
control.initialize(exp)

# Timing Calibration and Constants
# Assume 60 Hz monitor
t0 = exp.clock.time
exp.screen.update()
t1 = exp.clock.time
frame_duration_ms = t1 - t0
if frame_duration_ms == 0:
    frame_duration_ms = 16.67 

# Define constants for the experiment display
CIRCLE_RADIUS = 40
CIRCLE_DISTANCE = 120
STIM_DURATION_FRAMES = 12  # circle stays on screen ~ 200msec
LOW_ISI_FRAMES = 0         # Short gap for element motion 0msec
HIGH_ISI_FRAMES = 18       # Long gap for group motion ~300msec

# 2: Stimuli & Functions

def present_for(stims, frames):
    if frames <= 0:
        return  # Do nothing if duration is zero or less
    # Calculate the total target duration based on measured frame rate
    total_duration_ms = frames * frame_duration_ms

    # Draw all stimuli to the back buffer and update the screen.
    t0_draw = exp.clock.time
    exp.screen.clear()
    if stims: # Exclude empty stimuli
        for stim in stims:
            stim.present(clear=False, update=False)
    exp.screen.update()
    draw_time = exp.clock.time - t0_draw

    # Wait for the remaining time to meet the total target duration
    remaining_time = total_duration_ms - draw_time
    if remaining_time > 0:
        exp.clock.wait(remaining_time)

def make_circles(radius, distance, n=3, colour=(0, 0, 255)):
    circles = []
    for i in range(n):
        circle = stimuli.Circle(radius, colour=colour)
        circle.position = ((i - (n - 1) / 2) * distance, 0)
        circles.append(circle)
    return circles

def add_tags(circles, radius, tag_radius=8,
             colours=[(255, 0, 0), (0, 255, 0), (255, 255, 0)]):
    tagged = []
    for i, c in enumerate(circles): 
        circ = stimuli.Circle(radius, colour=c.colour, position=c.position)
        tag = stimuli.Circle(tag_radius, colour=colours[i % len(colours)])
        # Position the tag in the center of circle
        tag.position = (0, 0)
        # Plot the tag onto the new circle's surface
        tag.plot(circ)
        tagged.append(circ)
    return tagged

def run_trial(exp, radius, distance, isi_frames, with_tags):
    """Runs one Ternus trial with given parameters."""
    # Create the stimuli for the two animation frames
    frame1 = make_circles(radius, distance)
    # Frame 2 is shifted one position to the right
    frame2 = make_circles(radius, distance)
    for circle in frame2:
        circle.position = (circle.position[0] + distance, 0)
    
    # Replace circles with tagged versions if needed
    if with_tags:
        frame1 = add_tags(frame1, radius)
        frame2 = add_tags(frame2, radius)
    
    # Preload all stimuli into memory 
    for stim in frame1 + frame2:
        stim.preload()

    # ANIMATION
    while True:
        # Show the first frame of circles for the specified time duration
        present_for(frame1, STIM_DURATION_FRAMES)
        # Show a blank screen for the Inter-Stimulus Interval (ISI)
        present_for([], isi_frames)
        # Show the second frame of circles
        present_for(frame2, STIM_DURATION_FRAMES)
        # Show another blank screen for the ISI
        present_for([], isi_frames)
        # Check if the space is pressed to exit
        if exp.keyboard.check(K_SPACE):
            break

# 3: Execution
control.start()

# Trial 1: Low ISI
exp.screen.clear()
stimuli.TextLine("Trial 1: Element motion (low ISI). Press SPACE to start.", text_size=30).present()
exp.keyboard.wait(K_SPACE)
run_trial(exp, CIRCLE_RADIUS, CIRCLE_DISTANCE, LOW_ISI_FRAMES, with_tags=False)

# Trial 2: High ISI
exp.screen.clear()
stimuli.TextLine("Trial 2: Group motion (high ISI). Press SPACE to start.", text_size=30).present()
exp.keyboard.wait(K_SPACE)
run_trial(exp, CIRCLE_RADIUS, CIRCLE_DISTANCE, HIGH_ISI_FRAMES, with_tags=False)

# Trial 3: High ISI with tags
exp.screen.clear()
stimuli.TextLine("Trial 3: Element motion with tags (high ISI). Press SPACE to start.", text_size=30).present()
exp.keyboard.wait(K_SPACE)
run_trial(exp, CIRCLE_RADIUS, CIRCLE_DISTANCE, HIGH_ISI_FRAMES, with_tags=True)

stimuli.TextLine("Press SPACE to quit.", text_size=30).present()
exp.keyboard.wait(K_SPACE)
control.end()
