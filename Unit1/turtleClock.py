import turtle

wn = turtle.Screen()
clock = turtle.Turtle()
wn.bgcolor("lightgreen")
clock.shape("turtle")
clock.color("blue")
clock.pensize(3)
clock.speed(10)
clock.stamp()

for i in range(12):
    clock.penup()
    clock.forward(150)
    clock.pendown()
    clock.forward(10)
    clock.penup()
    clock.forward(10)
    clock.stamp()
    clock.forward(-170)
    clock.left(360/12)

wn.exitonclick()