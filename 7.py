#PythonDraw.py
import turtle
turtle.setup(1000,350,200,200)
turtle.penup()
turtle.fd(-300)
turtle.pendown()
turtle.pensize(30)
turtle.pencolor("tomato")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()