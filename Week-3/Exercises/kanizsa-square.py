import expyriment
from expyriment import design, control, stimuli
from expyriment.misc import constants
from expyriment.misc.constants import C_GREY

## 1: Global Setting
# set the color of screen to C_GREY
exp = expyriment.design.Experiment(
    name="Kanizsa Square",
    background_colour=constants.C_GREY
)
# Create an object of class Experiment:
control.initialize(exp)

control.set_develop_mode(True)
## 2: Design & Set Ups
# Extract screen dimensions
screen_width, screen_height = exp.screen.size 

# Set size of square, which is 25% of the screen width
square_side_length = 0.25 * screen_width
# Set size of circle
circle_radius_length = 0.05 * screen_width
# Find the position of Square/center of circles (from the screen center (0,0) to each circle center)
pos = square_side_length/2

# Create Stimuli
all_stimuli = []
for x in (-pos, pos):
    for y in (-pos, pos):
        # Define color of circles
        circle_color = constants.C_WHITE if y < 0 else constants.C_BLACK
        # Create circle according to the center
        circle = expyriment.stimuli.Circle(
            radius=circle_radius_length,
            position=(x, y),
            colour=circle_color
        )
        all_stimuli.append(circle)

        # Find the position of & Create the square 
        square = expyriment.stimuli.Rectangle(
            size=(square_side_length, square_side_length),
            position=(0, 0),
            colour=constants.C_GREY
        )
        all_stimuli.append(square)

# Preload the stimuli
for stim in all_stimuli:
    stim.preload()

# 3: Execution
expyriment.control.start()
# Create the canvas
canvas = expyriment.stimuli.Canvas(size=exp.screen.size)
for stim in all_stimuli:
    stim.plot(canvas)
canvas.present()

# Wait for any key to be pressed
exp.keyboard.wait()

# 3: Execution of stimuli & Start the experiment
expyriment.control.end()

