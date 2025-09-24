# 1: Global Setting
# Import the main modules of expyriment
from expyriment import design, control, stimuli

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name="Display Edges")
control.initialize(exp)
# 2: Stimuli and Design

# basic design of heights, widths 
width, height = exp.screen.size # acquire the height and width of screen
square_side_length = int(0.05 * width)  # 5% of the screen width
half_side = square_side_length / 2



# find the center of squares
position_x = width/2 - half_side 
position_y = height/2 - half_side

# find the position of squares
positions = [
    (-position_x, position_y),
    (position_x, position_y),
    (-position_x, -position_y),
    (position_x, position_y)
]
# generate the squares
for pos in positions:
    rectangle = stimuli.Rectangle(size=(square_side_length,
                                    square_side_length), 
                                    position = pos,
                                    line_width = 1,
                                    line_color=(255, 0, 0))
    square.plot(canvas)

canvas.present()

# Wait for any key to be pressed
exp.keyboard.wait()

# 3: End 
expyriment.control.end()
