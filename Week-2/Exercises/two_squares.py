# displays two squares side by side
# the left one red
#  the right one green
# Leave the fixation cross out.
# The two squares should be separated by 200 pixels but centered as a whole
#  Present them on-screen until a key is pressed.
from expyriment import design, control, stimuli

control.set_develop_mode()

# Create an object of class Experiment: 
# This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Two-squares")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# left red square
# Create a 50px-border Square
left_square = stimuli.Rectangle(size = (50,50), colour = (255, 0, 0), position = (-100, 0))

# right green square
right_square = stimuli.Rectangle(size = (50,50), colour = (0, 128, 0), position = (100, 0))

# start the experiment
control.start(subject_id=1)

# Present two squares on the screen
left_square.present(clear=True, update=False)
right_square.present(clear=False, update=True)


# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# end the experiment
control.end()
