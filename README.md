# Turtle Library

## What is Turtle?

Turtle is Python's built-in drawing tool that moves a virtual pen on a canvas using simple commands like `forward()`, `right()`, and `pencolor()` — teaching programming concepts visually by making the computer draw your code's logic.

Imagine you are holding a **marker** in your hand and there is a **white paper** in front of you. You can move the marker forward, turn it, lift it up, change its color. **Turtle does exactly this — but on a computer screen.** It is a virtual pen that draws whatever you command it to do.

## Demo 
https://github.com/user-attachments/assets/c685939a-3499-49dd-b928-3a5f5fd130da




---

## The Complete Life of Turtle — 5 Things It Can Do

---

### 1 — Moving

```python
forward(100)    # move 100 pixels forward — draws a line
backward(50)    # move 50 pixels backward — draws a line
```

Turtle starts at center of screen facing right. `forward(100)` moves it 100 pixels in whatever direction it is currently facing.

---

### 2 — Turning

```python
right(90)       # turn 90 degrees clockwise (to the right)
left(45)        # turn 45 degrees counter-clockwise (to the left)
```

Turning does NOT draw anything. It just changes the direction the turtle is facing. After turning, the next `forward()` will go in the new direction.

---

### 3 — Pen Up and Pen Down

```python
penup()         # lift the pen — turtle moves WITHOUT drawing
pendown()       # put pen down — turtle draws as it moves
```

This is the most important concept. By default pen is always down — so turtle draws everywhere it goes. When you lift the pen with `penup()` you can move to a new position without drawing an unwanted line. Always use `penup()` before jumping to a new position.

```python
from turtle import *

forward(100)    # line drawn here
penup()         # pen lifted
forward(50)     # NO line here — just moving
pendown()       # pen put back down
forward(100)    # line drawn again

done()
```

Result: one line, then a gap, then another line.

---

### 4 — Colors and Filling

```python
pencolor("red")       # color of the line being drawn
fillcolor("yellow")   # color that fills inside a shape
begin_fill()          # start recording the shape to fill
end_fill()            # fill the enclosed shape with fillcolor
```

To draw a filled yellow square:

```python
from turtle import *

pencolor("black")
fillcolor("yellow")
begin_fill()

for i in range(4):
    forward(100)
    right(90)

end_fill()
done()
```

---

### 5 — Screen Setup

```python
speed(0)          # how fast turtle draws
bgcolor("black")  # background color of the window
done()            # keep the window open when drawing finishes
```

---

## Speed — Full Explanation

```python
speed(1)    # slowest — good for learning, see every line being drawn
speed(5)    # medium speed
speed(10)   # fast
speed(0)    # instant — everything appears at once, no animation
```

Keep speed slow while learning so you can watch what is happening. Use speed 0 in final programs so it draws quickly.

---

## Sending Turtle to Any Position

```python
goto(200, 100)    # jump directly to coordinate (200, 100)
home()            # return to center (0, 0) facing right
```

Always use `penup()` before `goto()` otherwise turtle will draw a line all the way to that position.

```python
penup()
goto(200, 100)    # move without drawing
pendown()
forward(100)      # now draw from the new position
```

---

## The Coordinate System

```
         up (y+)
            |
            |
left -------+------- right (x+)
(x-)        |
            |
         down (y-)
```

Center of screen is `(0, 0)`. Going right increases X. Going up increases Y. Turtle starts at `(0, 0)` facing right.

---

## What Can You Build With Turtle

- Squares, triangles, circles, stars
- Colorful patterns and spirals
- Fractals like snowflakes
- Simple games like snake
- Animated step by step drawings
- Math and geometry visualizations

---

## The One Mental Model To Remember

Every time you look at turtle code, just think:

> "I am a person standing in a field holding a marker. The code is telling me — go forward, turn, change color, lift the pen."

That is all turtle is. Nothing more.

---


# Run command
python name of file.py
