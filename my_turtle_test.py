import turtle
import math
import time

# ── Screen ────────────────────────────────────────────────────────────────────
screen = turtle.Screen()
screen.title("🐢 Drawing Turtle Step by Step...")
screen.bgcolor("white")
screen.setup(width=720, height=560)
screen.tracer(1)
# turtle pen
t = turtle.Turtle()
t.hideturtle()
t.speed(10)
# text show on screen label
lbl = turtle.Turtle()
lbl.hideturtle()
lbl.penup()
lbl.speed(0)

def show_label(text):
    lbl.clear()
    lbl.goto(0, -230)
    lbl.pencolor("#444444")
    lbl.write(text, align="center", font=("Arial", 14, "bold"))

def pause(s):
    screen.tracer(0); screen.update()
    time.sleep(s)
    screen.tracer(1)

# ── Primitives ────────────────────────────────────────────────────────────────
def jump(x, y): t.penup(); t.goto(x, y)

def ellipse(cx, cy, rx, ry, fill, outline, lw=3):
    t.pensize(lw); t.pencolor(outline); t.fillcolor(fill)
    jump(cx + rx, cy); t.pendown(); t.begin_fill()
    for a in range(0, 361, 3):
        rad = math.radians(a)
        t.goto(cx + rx*math.cos(rad), cy + ry*math.sin(rad))
    t.end_fill()

def arc_line(cx, cy, rx, ry, a0, a1, col, lw=2):
    t.pencolor(col); t.pensize(lw)
    first = True
    for a in range(a0, a1 + 1):
        rad = math.radians(a)
        x = cx + rx*math.cos(rad)
        y = cy + ry*math.sin(rad)
        if first: jump(x, y); t.pendown(); first = False
        else: t.goto(x, y)
    t.penup()

def draw_line(x0, y0, x1, y1, col, lw=2):
    t.pencolor(col); t.pensize(lw)
    jump(x0, y0); t.pendown(); t.goto(x1, y1); t.penup()

# ── Palette ───────────────────────────────────────────────────────────────────
G   = "#5CB338"   # green
Y   = "#F2C915"   # yellow
BR  = "#C8640A"   # brown shell
BRD = "#7A3A00"   # dark brown lines on shell
BLK = "#111111"   # black outline

# ══════════════════════════════════════════════════════════════════════════════
# STEP 1 — Back Legs
# ══════════════════════════════════════════════════════════════════════════════
show_label("Step 1: Drawing back legs...")
ellipse(-118, -120, 42, 24, G, BLK, 3)
for dx in (-22, 0, 22): ellipse(-118+dx, -140, 14, 12, G, BLK, 3)
ellipse(138, -120, 42, 24, G, BLK, 3)
for dx in (-22, 0, 22): ellipse(138+dx, -140, 14, 12, G, BLK, 3)
pause(0.15)

# ══════════════════════════════════════════════════════════════════════════════
# STEP 2 — Yellow Belly
# ══════════════════════════════════════════════════════════════════════════════
show_label("Step 2: Drawing yellow belly...")
ellipse(10, -100, 160, 44, Y, BLK, 3)
pause(0.15)

# ══════════════════════════════════════════════════════════════════════════════
# STEP 3 — Green Body
# ══════════════════════════════════════════════════════════════════════════════
show_label("Step 3: Drawing green body...")
ellipse(10, -60, 158, 78, G, BLK, 3)
pause(0.15)

# ══════════════════════════════════════════════════════════════════════════════
# STEP 4 — Front Legs
# ══════════════════════════════════════════════════════════════════════════════
show_label("Step 4: Drawing front legs...")
ellipse(-158, -95, 36, 22, G, BLK, 3)
for dx in (-18, 0, 18): ellipse(-158+dx, -113, 13, 11, G, BLK, 3)
ellipse(174, -95, 36, 22, G, BLK, 3)
for dx in (-18, 0, 18): ellipse(174+dx, -113, 13, 11, G, BLK, 3)
pause(0.15)

# ══════════════════════════════════════════════════════════════════════════════
# STEP 5 — Shell Dome
# ══════════════════════════════════════════════════════════════════════════════
show_label("Step 5: Drawing brown shell...")
ellipse(10, -20, 148, 128, BR, BLK, 4)
# repaint green + yellow strip over bottom of shell
screen.tracer(0)
ellipse(10, -58, 156, 44, G, BLK, 3)
ellipse(10, -98, 158, 38, Y, BLK, 3)
screen.update(); screen.tracer(1)
# redraw shell bottom arc on top
arc_line(10, -20, 148, 128, 195, 345, BLK, 4)
pause(0.15)

# ══════════════════════════════════════════════════════════════════════════════
# STEP 6 — Shell Plate Lines  (FIXED — clean cartoon plate pattern)
#
#  Pattern (as seen in reference image):
#
#        |          <- centre vertical line from top to hub
#       / \         <- two ribs going from hub outward+downward
#      /   \
#  ___/     \___    <- bottom horizontal arc
#
#  Plus one small oval shape at the hub (centre diamond)
#  No random crossing arcs — clean and simple
# ══════════════════════════════════════════════════════════════════════════════
show_label("Step 6: Drawing shell plate lines (pencil)...")

HUB_X, HUB_Y = 10, 5   # centre hub where all lines meet

# 1) Centre vertical line — top of dome down to hub
draw_line(HUB_X, 104, HUB_X, HUB_Y, BRD, 2)
pause(0.08)

# 2) Left rib — from hub curves down-left to shell edge
arc_line(HUB_X - 68, HUB_Y, 68, 60, 0, 88, BRD, 2)
pause(0.08)

# 3) Right rib — mirror, from hub curves down-right
arc_line(HUB_X + 68, HUB_Y, 68, 60, 92, 180, BRD, 2)
pause(0.08)

# 4) Upper-left short rib — from hub up-left
arc_line(HUB_X - 42, HUB_Y + 50, 44, 38, 310, 360, BRD, 2)
arc_line(HUB_X - 42, HUB_Y + 50, 44, 38,   0,  50, BRD, 2)
pause(0.08)

# 5) Upper-right short rib — from hub up-right
arc_line(HUB_X + 42, HUB_Y + 50, 44, 38, 130, 230, BRD, 2)
pause(0.08)

# 6) Small centre oval at hub (the diamond/oval at centre of shell)
ellipse(HUB_X, HUB_Y - 10, 10, 16, BR, BRD, 2)
pause(0.08)

# ══════════════════════════════════════════════════════════════════════════════
# STEP 7 — Head
# ══════════════════════════════════════════════════════════════════════════════
show_label("Step 7: Drawing head...")
ellipse(-186, -38, 48, 46, G, BLK, 3)
pause(0.1)

# ══════════════════════════════════════════════════════════════════════════════
# STEP 8 — Eyes & Smile  (FIXED — added BOTH eyes)
#   Left head eye  → on the head circle (left side)
#   Right body eye → small eye visible on right side of body near shell edge
# ══════════════════════════════════════════════════════════════════════════════
show_label("Step 8: Adding eyes and smile...")

# --- LEFT EYE (on head) ---
ellipse(-174, -24,  9,  9, "white", BLK, 2)
ellipse(-173, -24,  5,  5, BLK, BLK, 1)
ellipse(-170, -26,  2,  2, "white", "white", 0)   # gleam

# --- RIGHT EYE (on head, slightly right of left eye) ---
ellipse(-158, -24,  9,  9, "white", BLK, 2)
ellipse(-157, -24,  5,  5, BLK, BLK, 1)
ellipse(-154, -26,  2,  2, "white", "white", 0)   # gleam

# --- SMILE (on head) ---
arc_line(-188, -46, 16, 11, 205, 335, BLK, 2)
pause(0.1)

# ══════════════════════════════════════════════════════════════════════════════
# STEP 9 — Tail
# ══════════════════════════════════════════════════════════════════════════════
show_label("Step 9: Drawing tail...")
ellipse(178, -60, 22, 15, G, BLK, 3)
pause(0.1)

# ══════════════════════════════════════════════════════════════════════════════
show_label("✅ Done! Turtle is ready! 🐢")
screen.update()
turtle.done()