
import turtle

wn = turtle.Screen()
userTurtle = turtle.Turtle()
myColors = ["red", "green", "pink", "yellow", "purple", "blue"]
myShapes = ["turtle", "circle", "arrow", "classic", "triangle", "square", "blank"]

userBgColor = input("Choose a background color: "+ str(myColors))
wn.bgcolor(userBgColor)
myColors.remove(userBgColor)
userColor = input("Choose a turtle line color:"+ str(myColors))
myColors.remove(userColor)
userFill = input("Choose a turtle fill color:"+ str(myColors))
userTurtle.fillcolor(userFill)

userShape = input("Choose a object shape:"+ str(myShapes))
userTurtle.shape(userShape)

userSpeed = int(input("Choose a speed:"))
userTurtle.speed(userSpeed)

userSides = int(input("Choose number of sides:"))
userDistance = int(input("Choose distance:"))
userAngle = 360/userSides

userTurtle.begin_fill()

for i in range(userSides):
    userTurtle.stamp()
    userTurtle.forward(userDistance)
    userTurtle.right(userAngle)
    userTurtle.forward(userDistance)

userTurtle.end_fill()
wn.exitonclick()
