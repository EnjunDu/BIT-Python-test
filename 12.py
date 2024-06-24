import turtle as op
op.setup(1000,900)
op.pencolor("black")
op.pensize(5)
for i in range(4):
    op.seth(-90*(i+1))
    op.fd(200)
    op.right(90)
    op.circle(-200,45)
    op.goto(0,0)
op.done()