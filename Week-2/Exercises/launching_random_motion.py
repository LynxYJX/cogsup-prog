# launching_random_motion.py

from expyriment import design, control, stimuli
import random
import math

def run_random_launch_trial(exp):
    # Setup
    square_size = (50, 50)
    radius = 300  # Radius of the circle for the target square
    speed = 6     # Speed of movement in pixels per frame

    # 1: Choose a random angle and calculate positions
    angle = random.uniform(0, 2 * math.pi)  # Get a random angle in radians

    # The "launcher" (green square) starts at the center
    launcher = stimuli.Rectangle(size=square_size, colour=(0, 255, 0), position=(0, 0))

    # The "target" (red square) is stationary on the circle
    target_x = radius * math.cos(angle)
    target_y = radius * math.sin(angle)
    target = stimuli.Rectangle(size=square_size, colour=(255, 0, 0), position=(target_x, target_y))

    # Show the initial state for 1 second
    launcher.present(clear=True, update=False)
    target.present(clear=False, update=True)
    exp.clock.wait(1000)

    # 2: Animate the launcher moving towards the target 
    # the launcher must travel the radius minus one side length.
    distance_to_travel = radius - square_size[0]
    distance_traveled = 0

    # Calculate the movement vector
    move_x = speed * math.cos(angle)
    move_y = speed * math.sin(angle)

    while distance_traveled < distance_to_travel:
        launcher.move((move_x, move_y))
        distance_traveled += speed
        # Redraw screen
        launcher.present(clear=True, update=False)
        target.present(clear=False, update=True)
        exp.clock.wait(16) # Pause for smooth animation

    # 3: Animate the target being launched 
    # It travels the same distance at the same speed. The launcher stays put.
    distance_traveled = 0
    while distance_traveled < distance_to_travel:
        target.move((move_x, move_y))
        distance_traveled += speed
        # Redraw screen
        launcher.present(clear=True, update=False)
        target.present(clear=False, update=True)
        exp.clock.wait(16)

    # Pause at the end of the trial
    exp.clock.wait(1000)


## Calls the function
control.set_develop_mode(True)
exp = design.Experiment(name="Random Motion Launching")
control.initialize(exp)
control.start(subject_id=1)

# Display three consecutive launching events
for i in range(3):
    # Show a title screen for each trial
    stimuli.TextLine(f"Trial {i + 1} of 3").present()
    exp.clock.wait(1500)
    # Run the trial
    run_random_launch_trial(exp)

# End the experiment
control.end()
