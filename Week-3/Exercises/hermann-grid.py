# hermann-grid.py
import expyriment
from expyriment import design, control, stimuli
from expyriment.misc import constants
from expyriment.misc.constants import C_GREY

# 1: Global Setting
exp = expyriment.design.Experiment(
    name="Hermann Grid",
    background_colour=constants.C_WHITE
)
expyriment.control.initialize(exp)
control.set_develop_mode(True)

# 2: Stimulus Setup
# Set the parameters
n_rows = 5
n_cols= 5
square_size = 60 
gap_size = 15   
square_colour = constants.C_BLACK

# Total grid dimensions
grid_width = n_cols* square_size + (n_cols- 1) * gap_size
grid_height = n_rows * square_size + (n_rows - 1) * gap_size

# Starting position for the center of the top-left square
start_x = -grid_width / 2 + square_size / 2
start_y = grid_height / 2 - square_size / 2

# Create Stimuli
grid_squares = []
# Create each square in the loop
for i in range(n_rows):
    for j in range(n_cols):
        # Calculate the center position for the square at (row, col)
        x = start_x + j * (square_size + gap_size)
        y = start_y - i * (square_size + gap_size)

        square = expyriment.stimuli.Rectangle(
            size=(square_size, square_size),
            position=(x, y),
            colour=square_colour
        )
        grid_squares.append(square)

# Preload
for square in grid_squares:
    square.preload()

# 3: Execution
expyriment.control.start()

canvas = expyriment.stimuli.Canvas(size=exp.screen.size)
for square in grid_squares:
    square.plot(canvas)
canvas.present()

exp.keyboard.wait()
expyriment.control.end()
