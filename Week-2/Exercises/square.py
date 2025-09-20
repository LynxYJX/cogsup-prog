
from expyriment import design, control, stimuli

control.set_develop_mode()

# Create an object of class Experiment
exp = design.Experiment(name="Square")

# Initialize the experiment
control.initialize(exp)

# Create a fixation cross
fixation = stimuli.FixCross()

# Create a 50x50 pixel blue square
square = stimuli.Rectangle(size=(50, 50), colour=(0, 0, 255))

# Start the experiment trial
control.start(subject_id=1)

# 1: Show the fixation cross on top of the square
square.present(clear=True, update=False)

# draw the fixation cross on top of it before updating the screen.
fixation.present(clear=False, update=True)

# Leave them on-screen for half a second (500 ms)
exp.clock.wait(500)

# 2: Show only the square
square.present(clear=True, update=True)

# Wait for any key to be pressed
exp.keyboard.wait()

# End the experiment session
control.end()
