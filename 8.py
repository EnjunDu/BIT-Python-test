import turtle as op
op.setup(1000,350)
op.penup()
op.fd(-250)
op.pendown()
op.pensize(25)
op.pencolor("purple")
op.seth(-40)
for i in range (4):
    op.circle(40,80)
    op.circle(-40,80)
op.circle(40,40)
op.fd(40)
op.circle(16,180)
op.fd(80/3)
op.done()