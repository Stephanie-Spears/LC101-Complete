import turtle

def drawSquare(myTurt, sideLen):
    for i in range(4):
        myTurt.forward(sideLen)
        myTurt.left(90)
        
def fence(myTurt, sideLen):
    for i in range(4):
        newXcor = myTurt.xcor()
        newYcor = myTurt.ycor()
        newPos = drawSquare(myTurt, sideLen)
        myTurt.penup()
        myTurt.goto(newXcor-10, newYcor-10)
        myTurt.pendown()
        sideLen+=20
    

wn = turtle.Screen()
wn.bgcolor("lightgreen")

fabio = turtle.Turtle()
fabio.pensize(3)
fabio.color("hotpink")
sideLen=20
fence(fabio, sideLen)
