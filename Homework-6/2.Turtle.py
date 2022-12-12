import turtle

pen= turtle.Pen()
turtle.bgcolor("black")
pen.shape("turtle")

n=3
line=3
side=100
pen.left(30)

for i in range(3):
    pen.pencolor("yellow")
    pen.left(120)
    pen.forward(100)

 
while line<=52:
    if n%2 == 1:
        pen.pencolor("blue")
    else:
        pen.pencolor("yellow")

    pen.right((((n-2)*180)/n)/2)
    pen.up()
    pen.forward(20)
    pen.down()
    n+=1
    pen.left((180-(((n-2)*180)/n)) + ((((n-2)*180)/n)/2))
    pen.forward(side+10)
    for j in range(1,n):
        pen.left(180-(((n-2)*180)/n))
        pen.forward(side+10)
    side+=10
line+=1

turtle.done()