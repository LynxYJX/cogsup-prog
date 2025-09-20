from expyriment import design, control, stimuli

def display_launching_event(exp, temporal_gap=0, spatial_gap=0, speed_ratio=1):

    # Create fresh stimuli for each trial to reset their positions
    left_square = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0), position=(-400, 0))
    right_square = stimuli.Rectangle(size=(50, 50), colour=(0, 255, 0), position=(0, 0))

    # 1: Present the initial state for 1 second
    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)
    exp.clock.wait(1000)

    # 2: Animate the left square
    # The target position is adjusted by the spatial_gap parameter
    target = -50 - spatial_gap
    step_size = 7  # Speed in pixels per frame

    while left_square.position[0] < target:
        left_square.move((step_size, 0))
        left_square.present(clear=True, update=False)
        right_square.present(clear=False, update=True)
        exp.clock.wait(16) # This pause is crucial for smooth animation

    # Apply the temporal gap, if any
    if temporal_gap > 0:
        exp.clock.wait(temporal_gap)

    # 3: Animate the right square moving away
    # Its speed is adjusted by the speed_ratio parameter
    right_speed = step_size * speed_ratio
    distance_to_travel = 350
    distance_traveled = 0

    while distance_traveled < distance_to_travel:
        right_square.move((right_speed, 0))
        distance_traveled += right_speed
        left_square.present(clear=True, update=False)
        right_square.present(clear=False, update=True)
        exp.clock.wait(16) # for smooth casuality

    # 4: Show the final display for 1 second
    exp.clock.wait(1000)


def show_title(exp, text):
    """A helper function to display a title on the screen."""
    title = stimuli.TextLine(text, text_size=32)
    title.present(clear=True, update=True)
    exp.clock.wait(2000)

# Calls the function and sets up the experiment

control.set_develop_mode(True)

exp = design.Experiment(name="Launching Function")
control.initialize(exp)
control.start(subject_id=1)

# case 1: Standard Michottean Launching
show_title(exp, "1. Standard Launching")
display_launching_event(exp, temporal_gap=0, spatial_gap=0, speed_ratio=1)

# case 2: Launching with a Temporal Gap
show_title(exp, "2. Temporal Gap (500ms)")
display_launching_event(exp, temporal_gap=500, spatial_gap=0, speed_ratio=1)

# case 3: Launching with a Spatial Gap
show_title(exp, "3. Spatial Gap (40px)")
display_launching_event(exp, temporal_gap=0, spatial_gap=40, speed_ratio=1)

# case 4: Triggering Event
show_title(exp, "4. Triggering (3x Speed)")
display_launching_event(exp, temporal_gap=0, spatial_gap=0, speed_ratio=3)

# End the experiment
control.end()
