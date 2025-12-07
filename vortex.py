import turtle
import math
import argparse

# Parse user arguments
parser = argparse.ArgumentParser(description="Draw vortex patterns with Python turtle graphics")
parser.add_argument("--radius", type=int, default=200, help="Circle radius")
parser.add_argument("--base", type=int, default=235, help="Number of points on the circle")
parser.add_argument("--multiplier", type=int, default=19, help="Multiplier for connecting points")
parser.add_argument("--color", type=str, default="black", help="Color of the points and lines")
parser.add_argument("--background_color", type=str, default="white", help="Background color of the window")
parser.add_argument("--show_dots", action='store_true', help="Show dots at each point")
parser.add_argument("--dot_size", type=int, default=5, help="Size of the points")
parser.add_argument("--show_numbers", action='store_true', help="Show point numbers")

# Assign arguments to variables
args = parser.parse_args()
base = args.base
multiplier = args.multiplier
color = args.color
background_color = args.background_color
show_dots = args.show_dots
dot_size = args.dot_size
show_numbers = args.show_numbers

# Prevent same color for points/lines and background
if color == background_color:
    print(f"\033[31mError: Color cannot be the same as background color.\033[0m") # red error
    exit(1)

# Limit radius to fit on screen and adjust window size
turtle.setup(1.0, 1.0) # full screen initially
screen = turtle.Screen() # get the screen with current Physical size
max_radius = min(screen.window_width(), screen.window_height()) // 2 - 20 # leave some margin
min_radius = 50
if args.radius > max_radius:
    radius = max_radius
    print(f"\033[33mWarning: radius too large, setting radius to {max_radius}\033[0m") # yellow warning
else:
    if args.radius < min_radius:
        radius = min_radius
        print(f"\033[33mWarning: radius too small, setting radius to {min_radius}\033[0m") # yellow warning
    else:
        radius = args.radius
    turtle.setup(radius * 2 + 40, radius * 2 + 40) # adjust window size based on radius

# Setup turtle
turtle.title(f'Vortex-{base}-{multiplier}')
pen = turtle.Turtle()
pen.speed(0)
pen.color(color)
turtle.bgcolor(background_color)

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
    numbers = [base-1] + list(range(1, base-1)) # start with base-1 instead of 0
    for i in numbers:
        angle = math.radians(-(i%(base-1)) * angle_between_points + 90) # i%(base-1) for the case were i=base-1 so it goes to 0 position
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
