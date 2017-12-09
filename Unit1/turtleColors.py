import turtle
import random

wn = turtle.Screen()
wn.bgcolor("blue")
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(8)
myTurtle.stamp()
myColors = ["red", "green", "pink", "yellow", "purple"] 


myTurtle.up()
myTurtle.goto(-100,150)
myTurtle.down()

for i in range(3):
    ranNum = random.randrange(0,5)

    myTurtle.color(myColors[ranNum])
    myTurtle.shape("triangle")
    myTurtle.stamp()
    myTurtle.forward(50)
    myTurtle.right(120)
    myTurtle.forward(50)
    
myTurtle.up()
myTurtle.goto(50, -50)
myTurtle.down()

for i in range(4):
    ranNum = random.randrange(0,5)

    myTurtle.color(myColors[ranNum])

    myTurtle.shape("square")
    myTurtle.stamp()
    myTurtle.forward(100)
    myTurtle.right(90)

myTurtle.up()
myTurtle.goto(-150, 0)
myTurtle.down()

for i in range(6):
    ranNum = random.randrange(0,5)

    myTurtle.color(myColors[ranNum])

    myTurtle.shape("arrow")
    myTurtle.stamp()
    myTurtle.forward(100)
    myTurtle.right(60)
    myTurtle
    
myTurtle.up()
myTurtle.goto(50, 150)
myTurtle.down()

for i in range(8):
    ranNum = random.randrange(0,5)

    myTurtle.color(myColors[ranNum])

    myTurtle.shape("circle")
    myTurtle.stamp()
    myTurtle.forward(60)
    myTurtle.right(45)


wn.exitonclick()
