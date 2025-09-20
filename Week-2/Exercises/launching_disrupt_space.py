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
exp = design.Experiment(name = "Launching")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

## define the spatial gap
# even a small gap will disturb the casuality; it seems like spatial_gap = 5 is the threshold
spatial_gap = 5


# left red square
# Create a 50px-border Square
left_square = stimuli.Rectangle(size = (50,50), colour = (255, 0, 0), position = (-400, 0))

# right green square
right_square = stimuli.Rectangle(size = (50,50), colour = (0, 128, 0), position = (0, 0))

# Start experiment
control.start(subject_id=1)

# 1: Present the initial state for 1 second
left_square.present(clear = True, update = False)
right_square.present(clear = False, update = True)
exp.clock.wait(1000)

# 2: Animate the left square to the right one
target = -50 - spatial_gap ## the distance of touch of squares; the spatial gap appears at the collision
step_size = 10 # set the speed

while left_square.position[0] < target:
    left_square.move((step_size, 0))
    # redraw the screen 
    left_square.present(clear = True, update = False)
    right_square.present(clear = False, update = True)

# 3: right square moving away
distance_travel = 400
traveled_distance = 0

while traveled_distance < distance_travel:
    right_square.move((step_size, 0))
    traveled_distance += step_size
    # redraw the screen
    left_square.present(clear = True, update = False)
    right_square.present(clear = False, update = True)

# 4: show the final displace for 1sec
exp.clock.wait(1000)

# end the experiment
control.end()
