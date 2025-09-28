# Import the main modules of expyriment
import expyriment
from expyriment import design, control, stimuli
from expyriment.misc import constants
from expyriment.misc.constants import C_GREY

# 1: Global Setting
# Create an object of class Experiment
exp = design.Experiment(name="Squares at Edges")
control.set_develop_mode(on=True)  # Toggle to check scaling independence
control.initialize(exp)

# 2: Design & Set Ups
# Get the screen dimensions
screen_width, screen_height = exp.screen.size

# Find the length of the square: 5% of screen width
square_len = 0.05 * screen_width
square_size = (square_len, square_len)

# Find centers of these squares
half_w = screen_width / 2 - square_len / 2
half_h = screen_height / 2 - square_len / 2

# Compute squares' centers
positions = []
for x in (-screen_width, screen_width):
    for y in (-screen_height, screen_height):
        # Ddetermine the direction by the sign of x and y.
        sign_x = 1 if x > 0 else -1
        sign_y = 1 if y > 0 else -1
        
        adjusted_x = (x / 2) - (sign_x * square_len / 2)
        adjusted_y = (y / 2) - (sign_y * square_len / 2)
        
        positions.append((adjusted_x, adjusted_y))

# Create stimuli
squares = [expyriment.stimuli.Rectangle(
    size=square_size,
    position=pos,
    colour=constants.C_RED,
    line_width=1) for pos in positions]

# Preload all stimuli to prevent loading
for square in squares:
    square.preload()

# 3: Execution of stimuli & Start the experiment
expyriment.control.start()

# Create the canvas
canvas = expyriment.stimuli.Canvas(size=exp.screen.size)

for square in squares:
    square.plot(canvas)
# Update the screen
canvas.present()

# Wait till key press
exp.keyboard.wait()

# End the experiment
expyriment.control.end()
