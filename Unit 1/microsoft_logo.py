# microsoft_logo.py

# Written by @zmagsar
# Nov 17, 2020
# Non-function version

import turtle as t

t.speed(0)

# Red square
t.penup()
t.goto(-250, 0)
t.pendown()
t.color("orange red")
t.begin_fill()
for x in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()
        
# Blue square
t.penup()
t.goto(-250, -55)
t.pendown()
t.color("deep sky blue")
t.begin_fill()
for x in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

# Green square
t.penup()
t.goto(-195, 0)
t.pendown()
t.color("yellow green")
t.begin_fill()
for x in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

# Yellow square
t.penup()
t.goto(-195, -55)
t.pendown()
t.color("gold")
t.begin_fill()
for x in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

# Microsoft writing
t.penup()
t.goto(-120, -50)
t.pendown()
t.pencolor("grey")
t.write("Microsoft", font = ("Segoe", 80, "normal"))
    
t.hideturtle()