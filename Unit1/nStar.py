
import turtle

def nStar(fabio, n):
    for i in range(n):
        fabio.forward(100)
        fabio.right(180-(180/n))#180 ----> minus the inner angle of a star point

def fiveStars(fabio):
    n = 9
    for i in range(5):
        nStar(fabio, n)
        fabio.penup()
        fabio.forward(350)
        fabio.right(144)
        fabio.pendown()

wn = turtle.Screen()
wn.bgcolor("lightgreen")
fabio = turtle.Turtle()
fabio.pensize(3)
fabio.color("hotpink")
fabio.up()
fabio.goto(-200,0)
fabio.down()
fabio.speed(10)

fiveStars(fabio)





