
from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math 

control.set_develop_mode()

exp = design.Experiment(name="Labeled Shapes")

control.initialize(exp)

# 1. Left Shape: Purple Equilateral Triangle
SIDE_LENGTH = 50
# R = s / (2 * sin(pi / n))
triangle_radius = SIDE_LENGTH / (2 * math.sin(math.pi / 3))
triangle_vertices = geometry.vertices_regular_polygon(3, triangle_radius)
triangle = stimuli.Shape(
    position=(-100, 0),
    vertex_list=triangle_vertices,
    colour=(128, 0, 128) 
)
# Get the triangle's actual height for matching the hexagon
triangle_height = triangle.surface_size[1]


# 2. Right Shape: Yellow Regular Hexagon
# The height of a point-up regular hexagon is 2 * Radius .
hexagon_radius = triangle_height / 2
# FIX: Arguments are now positional (no keywords)
hexagon_vertices = geometry.vertices_regular_polygon(6, hexagon_radius)
hexagon = stimuli.Shape(
    position=(100, 0),
    vertex_list=hexagon_vertices,
    colour=(255, 255, 0)  # Yellow
)


# 3. Vertical Lines
# The line starts from the top of the shape and goes up by 50px.
# Top of a shape = shape_y_position + shape_height / 2
line_triangle = stimuli.Line(
    start_point=(-100, triangle_height / 2),
    end_point=(-100, triangle_height / 2 + 50),
    line_width=3,
    colour=(255, 255, 255)  # White
)

line_hexagon = stimuli.Line(
    start_point=(100, triangle_height / 2),
    end_point=(100, triangle_height / 2 + 50),
    line_width=3,
    colour=(255, 255, 255)  # White
)


# 4. Shape Labels
# The label is positioned 20px above the end of the line segment.
label_triangle = stimuli.TextLine(
    text="triangle",
    position=(-100, triangle_height / 2 + 50 + 20),
    text_colour=(255, 255, 255)  # White
)

label_hexagon = stimuli.TextLine(
    text="hexagon",
    position=(100, triangle_height / 2 + 50 + 20),
    text_colour=(255, 255, 255)  # White
)


## --- Presentation --- ##

# Create a blank screen canvas to plot all stimuli onto for simultaneous presentation
canvas = stimuli.BlankScreen()
triangle.plot(canvas)
hexagon.plot(canvas)
line_triangle.plot(canvas)
line_hexagon.plot(canvas)
label_triangle.plot(canvas)
label_hexagon.plot(canvas)

# Start the experiment
control.start(subject_id=1)

# Present the canvas with all the plotted stimuli
canvas.present()

# Wait for a key press from the user
exp.keyboard.wait()

# End the experiment
control.end()
