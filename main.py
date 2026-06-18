import colorsys 
import turtle

# 1. Set tracer to 1 (or True) so every movement is shown immediately
# Your original code used 10, which skipped frames to go faster.
turtle.tracer(3)

turtle.bgcolor("black")

# 2. Set speed to 1, which is the slowest animation speed in Turtle
turtle.speed(1)

h = 0
for i in range(15):
    for j in range(18):
        # Generate the color
        c = colorsys.hsv_to_rgb(h, 1, 1)
        turtle.color(c)
        h += 0.005
        
        # Drawing the pattern
        turtle.rt(90)
        turtle.circle(150 - j * 6, 90)
        turtle.lt(90)
        turtle.circle(150 - j * 6, 90)
        turtle.rt(180)
    
    turtle.circle(40, 24)

turtle.done()