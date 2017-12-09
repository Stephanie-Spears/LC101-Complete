import turtle

def drawStar(fabio):
    for i in range(5):
        fabio.forward(100)
        fabio.right(180-36)#180 ----> minus the inner angle of a star point

def fiveStars(fabio):
    for i in range(5):
        drawStar(fabio)
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




