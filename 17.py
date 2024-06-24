import turtle
turtle.speed(20)
turtle.delay(0)
turtle.bgcolor('black')  # 设置背景颜色为black
sides = 6
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']
for x in range(360):
    turtle.pencolor(colors[x % sides])
    turtle.forward(x * 3 / sides + x)
    turtle.left(360 / sides + 1)
    turtle.width(x * sides / 200)
    turtle.left(90)
turtle.done()
