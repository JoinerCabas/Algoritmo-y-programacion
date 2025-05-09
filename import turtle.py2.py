import turtle
import colorsys

t = turtle.Turtle()
turtle.bgcolor("black")
t.pensize(2)
t.speed(0)
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    t.forward(i)
    t.right(100)
    h += 0.002
t.speed(3)
t.pensize(10)
#J
t.penup()
t.goto(-450, -80 + 120)
t.setheading(270)
t.pendown()
t.color("aqua")
t.forward(100)
t.circle(-25, 180)

#O
t.penup()
t.goto(-350, -80)
t.setheading(0)
t.pendown()
t.color("lime")
t.circle(60)

#I
t.penup()
t.goto(-250, -80)
t.setheading(90)
t.pendown()
t.color("pink")
t.forward(120)

#N
t.penup()
t.goto(-210, -80)
t.setheading(90)
t.pendown()
t.color("yellow")
t.forward(120)
t.right(135)
t.forward(170)
t.left(135)
t.forward(120)

#E
t.penup()
t.goto(-50, -80 + 120)  
t.setheading(270)
t.pendown()
t.color("black")
t.forward(120)      
t.backward(60)
t.left(90)
t.forward(40)       
t.backward(40)
t.right(90)
t.backward(60)
t.left(90)
t.forward(60)       
t.penup()
t.goto(-50, -200 + 120)
t.setheading(0)
t.pendown()
t.forward(60)       

#R
t.penup()
t.goto(50, -80)
t.setheading(90)
t.pendown()
t.color("orange")
t.forward(120)
t.right(90)
t.circle(-40, 180)
t.left(135)
t.forward(70)

t.hideturtle()
turtle.done()