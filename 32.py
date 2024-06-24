import turtle as a
import time
a.delay(10)
a.speed(10)
def drawGap():
    a.penup()
    a.fd(5)
def drawLine(draw):#绘制单端数码管
    drawGap()
    a.pendown() if draw else a.penup()
    a.fd(40)
    drawGap()
    a.right(90)
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    a.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    a.left(180)
    a.penup()
    a.fd(20)
def drawDate(date):
    a.pencolor("red")
    for i in date:
        if i =='-':
            a.write("年",font=("Arial",18,"normal"))
            a.pencolor("green")
            a.fd(40)
        elif i == '=':
            a.write("月",font=("Arial",18,"normal"))
            a.fd(40)
        elif i =='+':
            a.write("日",font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i))
def main():
    a.setup(1000,550,200,200)
    a.penup()
    a.fd(-300)
    a.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    a.hideturtle()
    a.done()
main()