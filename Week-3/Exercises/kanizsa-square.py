from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY

## 1: Global Setting
# set the color of screen to C_GREY
classexpyriment.io.Screen(colour: C_GREY) # ?
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name="Display Edges")
control.initialize(exp)

## 2: Design & Set Ups
# Extract screen coordinates
w, h = exp.screen.size
# Set size of square
square_side_length = 0.25 * w
# Set size of circle
circle_radius_length = 0.05 * w
# Find the position of Square



# Wait for any key to be pressed
exp.keyboard.wait()

# 3: End 
expyriment.control.end()
