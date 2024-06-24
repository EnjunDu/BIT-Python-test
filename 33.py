import turtle
turtle.delay(0)
turtle.speed(0)
def koch(size, n):
    if n==0:
        turtle. fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)
def main():
    turtle . setup( 800, 800)
    turtle . penup( )
    turtle. goto(-200, 20)
    turtle . pendown( )
    turtle. pensize(2)
    level = 3
    koch(400, level)
    # 3阶科赫曲线，阶数
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400, level)
    turtle. hideturtle( )
    turtle.done()
main()