import turtle as a
import time

def drawGap():
    a.penup()
    a.fd(5)
def drawLine1(draw):#绘制单端数码管
    drawGap()
    a.pendown() if draw else a.penup()
    a.fd(40)
    drawGap()
    a.right(75)
def drawLine2(draw):#绘制单端数码管
    drawGap()
    a.pendown() if draw else a.penup()
    a.fd(40)
    drawGap()
    a.right(105)
def drawDigit(digit):
    drawLine2(True) if digit in [2,3,4,5,6,8,9] else drawLine2(False)
    drawLine1(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine1(False)
    drawLine2(True) if digit in [0,2,3,5,6,8,9] else drawLine2(False)
    drawLine1(True) if digit in [0,2,6,8] else drawLine1(False)
    a.left(75)
    drawLine1(True) if digit in [0,4,5,6,8,9] else drawLine1(False)
    drawLine2(True) if digit in [0,2,3,5,6,7,8,9] else drawLine2(False)
    drawLine1(True) if digit in [0,1,2,3,4,7,8,9] else drawLine1(False)
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