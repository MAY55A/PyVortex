import turtle
import math
import argparse

# Parse user arguments
parser = argparse.ArgumentParser(description="Draw vortex patterns with Python turtle graphics")
parser.add_argument("--radius", type=int, default=200, help="Circle radius")
parser.add_argument("--base", type=int, default=235, help="Number of points on the circle")
parser.add_argument("--multiplier", type=int, default=19, help="Multiplier for connecting points")
parser.add_argument("--color", type=str, default="black", help="Color of the points and lines")
parser.add_argument("--show_dots", action='store_true', help="Show dots at each point")
parser.add_argument("--dot_size", type=int, default=5, help="Size of the points")
parser.add_argument("--show_numbers", action='store_true', help="Show point numbers")
args = parser.parse_args()

radius = args.radius
base = args.base
multiplier = args.multiplier
color = args.color
show_dots = args.show_dots
dot_size = args.dot_size
show_numbers = args.show_numbers

# Setup turtle
turtle.setup(800, 800)
turtle.title(f'Vortex-{base}-{multiplier}')
pen = turtle.Turtle()
pen.speed(0)
pen.color(color)

# Function to draw points on the circumference
def draw_points_on_circle(radius, base):
    points = []
    pen.penup()
    pen.goto(0, -radius)
    pen.pendown()
    pen.circle(radius)

    # Calculate the angle between each point
    angle_between_points = 360 / (base-1)

    # Draw points on the circumference
    for i in range(base-1):
        angle = math.radians(-i * angle_between_points + 90)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        points.append((x, y))
        if show_dots:
            # Move to the point and draw a small dot
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.dot(dot_size, color)
        if show_numbers:
            # Write the point number
            font_size = max(8, min(16, int((radius / base) * 2))) # Adjust font size based on radius and number of points
            label_offset = font_size  # distance outside the circle
            label_x = x + label_offset * math.cos(angle)
            label_y = y + label_offset * math.sin(angle)

            # Adjust vertically for bottom half of the circle
            if base//4 < i < 3*base//4 :
                label_y -= label_offset 

            pen.penup()
            pen.goto(label_x, label_y)
            pen.write(str(i), align="center", font=("Arial", font_size, "normal"))

    return points

# Function to draw lines between points
def draw_lines(points, multiplier, base) :
    for i in range(1,len(points)) :
        pen.penup()
        pen.goto(points[i])
        pen.pendown()
        pen.goto(points[(i*multiplier)%(base-1)])
        

# Draw vortex
draw_lines(draw_points_on_circle(radius, base), multiplier, base)

pen.hideturtle()
turtle.done()
