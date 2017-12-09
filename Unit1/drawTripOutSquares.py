import turtle

def tripOut(fabio, someangle):
    somedist = 1
    for i in range(80):       
        fabio.forward(somedist)
        fabio.right(someangle)
        somedist += 2

wn=turtle.Screen()
wn.bgcolor("lightgreen")
fabio = turtle.Turtle()
fabio.color("blue")
fabio.penup()
fabio.goto(-100,0)
fabio.pendown()
fabio.speed(20)

angle = 90
angle2 = 89
tripOut(fabio, angle)
fabio.penup()
fabio.goto(100, 0)
fabio.pendown()
tripOut(fabio, angle2)

