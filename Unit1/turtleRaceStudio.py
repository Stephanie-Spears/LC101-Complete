import turtle              # 1. import the modules
import random
wn = turtle.Screen()       # 2. Create a screen
wn.bgcolor('lightblue')

def flagGirl():
    flagGirl = turtle.Turtle()
    flagGirl.speed(10)
    flagGirl.shape("turtle")
    flagGirl.color("hotpink")
    flagGirl.pensize(4)
    flagGirl.pencolor("red")

    flagGirl.penup()
    flagGirl.goto(125,-210)
    flagGirl.left(90)

    for i in range(20):
        flagGirl.forward(15)
        flagGirl.penup()
        flagGirl.forward(5)
        flagGirl.pendown()
        


def createTurtle(startPoint, numOfTurtles):
    
    aTurtle = turtle.Turtle()

    colors = ["red", "blue", "green", "yellow", "purple", "violet", "maroon", "black", "white"]
    aTurtle.shape("turtle")
    aTurtle.speed(random.randrange(4,10))
    aTurtle.color(colors[random.randrange(0,(len(colors)))])

    aTurtle.penup()  
    aTurtle.goto(-200, startPoint) 
    aTurtle.pendown()

    return aTurtle

flagGirl()

numOfTurtles = random.randint(2,9)
turtleIndex = list(range(0, numOfTurtles))

a = {}
startPoint = 175
    
for i in range(0, numOfTurtles):
    key = "Turtle" + str(i)
    a[key] = createTurtle(startPoint, numOfTurtles)
    startPoint = startPoint - (400/(numOfTurtles))
    print("{}'s speed is: {}".format(key, a[key].speed()))



    
def winner():
    dist = 0
    while dist < 400:
        for i in range(0, numOfTurtles):
            if int(a["Turtle" + str(i)].xcor())>125:
                return ("{} wins! Suck it losers!".format("Turtle" + str(i)))
            else:
                dist = (a["Turtle" + str(i)]).speed()
                a["Turtle" + str(i)].forward(dist)
print(winner())
        


    
wn.exitonclick()
