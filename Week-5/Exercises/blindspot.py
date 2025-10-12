import os
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK
from expyriment.misc import constants

## Create the data folder to store the collected data in file.xpd
# Get the path
script_dir = os.path.dirname(os.path.abspath(__file__))
# Change the current working directory to the script's
os.chdir(script_dir)

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode(True)
control.initialize(exp)

# Define the headers for the data output file
exp.data_variable_names = [
    "eye",          # Eye tested
    "keypress",     # Key pressed
    "r",            # current radius of the circle
    "x_coord",      # current horizontal coordinate (x) of the circle
    "y_coord"       # current vertical coordinate (y) of the circle
]

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

def show_instructions(side):
    # Displays instructions
    eye_to_cover = "left" if side == "right" else "right"
    fixation_side = "left" if side == "right" else "right"
    
    instructions_text = (
        f"This trial will locate the blind spot for your {side} eye.\n\n"
        f"1. Please cover your {eye_to_cover} eye with your hand.\n\n"
        f"2. Keep your focus on the fixation cross on the {fixation_side} of the screen.\n\n"
        "3. Use ARROW KEYS to move the circle until it disappears.\n\n"
        "4. Use 1 to make the circle smaller and 2 to make it larger.\n\n"
        "Press the SPACEBAR to continue."
    )
    stimuli.TextScreen("Instructions", instructions_text, text_justification=0).present()
    exp.keyboard.wait()

""" Experiment """
def run_trial(side):
    # Set starting positions based on which eye being tested
    fixation_pos_x = -300 if side == "right" else 300
    circle_start_pos_x = 300 if side == "right" else -300
    
    # Create stimuli based on the template structure
    fixation = stimuli.FixCross(size=(50, 50), line_width=4, position=(fixation_pos_x, 0))
    fixation.preload()

    radius = 75
    circle = make_circle(r=radius, pos=(circle_start_pos_x, 0))
    
    # Step sizes for movement and resizing
    move_step = 5
    resize_step = 5

    # Stimulus presentation and keyboard checking
    running = True
    while running:
        fixation.present(clear=True, update=False)
        circle.present(clear=False, update=True)
        
        # Check for keyboard input
        key = exp.keyboard.check()
        
        if key is not None:
            collect_key = "N/A"
            
            # Movement of circle
            if key == constants.K_LEFT:
                circle.move((-move_step, 0))
                collect_key = "left"
            elif key == constants.K_RIGHT:
                circle.move((move_step, 0))
                collect_key = "right"
            elif key == constants.K_UP:
                circle.move((0, move_step))
                collect_key = "up"
            elif key == constants.K_DOWN:
                circle.move((0, -move_step))
                collect_key = "down"
            
            # Resizing
            elif key == ord('1'):
                new_r = max(5, circle.radius - resize_step)
                circle = make_circle(r=new_r, pos=circle.position)
                collect_key = "1"
            elif key == ord('2'):
                new_r = circle.radius + resize_step
                circle = make_circle(r=new_r, pos=circle.position)
                collect_key = "2"
            
            # Trial end
            elif key == constants.K_SPACE:
                running = False
                continue

            # Collect data for every valid keypress
            if collect_key != "N/A":
                exp.data.add([
                    side,
                    collect_key,
                    circle.radius,
                    circle.position[0],
                    circle.position[1]
                ])


""" Main Execution """
control.start(subject_id=1)

show_instructions("right")
run_trial("right")

show_instructions("left")
run_trial("left")
    
control.end()

