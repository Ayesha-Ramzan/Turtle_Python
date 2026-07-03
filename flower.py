from turtle import *
import colorsys

# Set the speed of drawing and background color
speed(0)
bgcolor("black")

# Initialize hue value
h = 0

# Outer loop for 16 repetitions
for i in range(16):
    # Inner loop for drawing 18 shapes
    for j in range(18):
        # Get the color using HSV to RGB conversion
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)

        # Increment hue for the next color
        h += 0.005
        
        # Draw shapes
        right(90)
        circle(150 - j * 6, 90)
        left(90)
        circle(150 - j * 6, 90)
        right(180)
        circle(40, 24)

# Complete the drawing
done()




#from turtle import *       # Import all turtle functions directly (no need to write turtle.speed, just speed)
#import colorsys            # Import colorsys to convert HSV color model to RGB (needed by turtle)

#speed(0)                   # Set drawing speed to maximum (0 = instant, no animation delay)
#bgcolor("black")           # Set background color to black (makes rainbow colors pop with contrast)

#h = 0                      # Initialize hue at 0.0 (red) — will cycle through full rainbow as it increases

#for i in range(16):        # Outer loop: repeat entire pattern 16 times to build dense layered mandala
#for j in range(18):    # Inner loop: draw 18 petal units per repetition, each slightly smaller

#c = colorsys.hsv_to_rgb(h, 1, 1)  # Convert hue h to RGB color — S=1 (vivid), V=1 (bright)
#color(c)                           # Set pen color to the RGB tuple c — each arc gets unique rainbow color

#h += 0.005         # Advance hue by 0.005 — small step = smooth color gradient across all 288 arcs

#right(90)                        # Turn turtle 90° clockwise — orients turtle for first arc direction
#circle(150 - j * 6, 90)         # Draw 90° arc — radius shrinks from 150 to 48 as j increases (nested petals)
#left(90)                         # Turn turtle 90° counter-clockwise — mirrors direction for second arc
#circle(150 - j * 6, 90)         # Draw second 90° arc — same shrinking radius, forms S-shaped petal with first arc
#right(180)                       # Turn turtle 180° — reverses direction, causes pattern to spiral and rotate
#circle(40, 24)                   # Draw tiny 24° arc with fixed radius 40 — slightly shifts turtle heading each time
#                                          # THIS is the secret: accumulated tiny rotations spread petals into full mandala circle

# done()                     # Keep the window open after drawing completes — required or window closes instantly