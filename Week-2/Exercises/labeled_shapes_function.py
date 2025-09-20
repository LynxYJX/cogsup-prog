
from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math


def create_labeled_polygon(n, side_length, color, position, label_text):
    # 1. Calculate the radius from the side length to create the polygon
    # R = s / (2 * sin(pi / n))
    radius = side_length / (2 * math.sin(math.pi / n))
    vertices = geometry.vertices_regular_polygon(n, radius)
    shape = stimuli.Shape(
        position=position,
        vertex_list=vertices,
        colour=color
    )
    shape_height = shape.surface_size[1]
    shape_x, shape_y = position

    # 2. Create the vertical line positioned on top of the shape
    line = stimuli.Line(
        start_point=(shape_x, shape_y + shape_height / 2),
        end_point=(shape_x, shape_y + shape_height / 2 + 50),
        line_width=3,
        colour=(255, 255, 255)  
    )

    # 3. Create the text label positioned above the line
    label = stimuli.TextLine(
        text=label_text,
        position=(shape_x, shape_y + shape_height / 2 + 50 + 20),
        text_colour=(255, 255, 255)  
    )

    return shape, line, label

control.set_develop_mode(True)
exp = design.Experiment(name="Labeled Shapes with Function")
control.initialize(exp)

# 1. Create the purple triangle
triangle, line_triangle, label_triangle = create_labeled_polygon(
    n=3,
    side_length=50,
    color=(128, 0, 128), 
    position=(-100, 0),
    label_text="triangle"
)

# 2. Create the yellow hexagon with matching height
# get the triangle's height
triangle_height = triangle.surface_size[1]
# calculate the required side length for that hexagon
# hexagon height: h = s * sqrt(3), so s = h / sqrt(3)
hexagon_side_length = triangle_height / math.sqrt(3)

hexagon, line_hexagon, label_hexagon = create_labeled_polygon(
    n=6,
    side_length=hexagon_side_length,
    color=(255, 255, 0),  
    position=(100, 0),
    label_text="hexagon"
)

# use of function

canvas = stimuli.BlankScreen()
for stim in [triangle, line_triangle, label_triangle,
             hexagon, line_hexagon, label_hexagon]:
    stim.plot(canvas)

control.start(subject_id=1)
canvas.present()
exp.keyboard.wait()
control.end()
