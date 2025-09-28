import expyriment
from expyriment import design, control, stimuli
from expyriment.misc import constants
from expyriment.misc.constants import C_GREY

def display_kanizsa_rectangle(aspect_ratio=1.5, rect_scale=0.4, circle_scale=0.05):
    # 1: Setup
    exp = expyriment.design.Experiment(
        name="Kanizsa Rectangle",
        background_colour=constants.C_GREY
    )
    expyriment.control.initialize(exp)
    control.set_develop_mode(True)
    # 2: Stimulus & Design
    screen_width, screen_height = exp.screen.size 

    # Set size of rectangle
    rect_width = screen_width * rect_scale
    rect_height = rect_width / aspect_ratio
    # Set the size of circle
    circle_radius = screen_width * circle_scale
    # Find the position
    x_offset = rect_width / 2
    y_offset = rect_height / 2

    # Create Stimuli
    all_stimuli = []
    for x in (-x_offset, x_offset):
        for y in (-y_offset, y_offset):
            # Define color of circles
            circle_color = constants.C_WHITE if y < 0 else constants.C_BLACK
            # Create circle according to the center
            circle = expyriment.stimuli.Circle(
                radius=circle_radius,
                position=(x, y),
                colour=circle_color
            )
            all_stimuli.append(circle)

            # Find the position of & Create the square 
            rectangle = expyriment.stimuli.Rectangle(
                size=(rect_width, rect_height),
                position=(0, 0),
                colour=constants.C_GREY
            )
            all_stimuli.append(rectangle)

    # Preload the stimuli
    for stim in all_stimuli:
        stim.preload()
    
    # 3: Execution
    expyriment.control.start()
    # Create canvas
    canvas = expyriment.stimuli.Canvas(size=exp.screen.size)
    for stim in all_stimuli:
        stim.plot(canvas)
    canvas.present()
    # Wait till keyboard is pressed
    exp.keyboard.wait()
    expyriment.control.end()
# Run the script
if __name__ == "__main__":
    display_kanizsa_rectangle(aspect_ratio=2.0, rect_scale=0.5, circle_scale=0.06)
