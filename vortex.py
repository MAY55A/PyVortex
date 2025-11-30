import turtle
import math
import argparse

# Parse user arguments
parser = argparse.ArgumentParser(description="Draw vortex patterns with Python turtle graphics")
parser.add_argument("--radius", type=int, default=200, help="Circle radius")
parser.add_argument("--base", type=int, default=235, help="Number of points on the circle")
parser.add_argument("--multiplier", type=int, default=19, help="Multiplier for connecting points")
args = parser.parse_args()

radius = args.radius
base = args.base
multiplier = args.multiplier

# Setup turtle
turtle.setup(800, 800)
turtle.title(f'Vortex-{base}-{multiplier}')
pen = turtle.Turtle()
pen.speed(10)

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
        # Move to the point and draw a small dot
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.dot(5, "black")  # 5 is the size of the dot, "red" is the color
        
        # Write the point number next to the dot
        '''
        pen.penup()
        pen.goto(x + 10, y)  # Adjust the position to avoid overlap with the dot
        pen.write(str(i), font=("Arial", 12, "normal"))  # Write the point number
        '''
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
