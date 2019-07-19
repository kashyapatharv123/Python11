from turtle import *

def sq():
    for i in range(4):
        t.forward(100)
        t.left(90)

t=Turtle()
wn=Screen()
wn.title("My turtle")
#wn.bgcolor("yellow")
#wn.bgpic("test.gif")
t.shape("turtle")
t.color("green","red")
t.speed(1)
t.begin_fill()
sq()
t.penup()
t.forward(100)
t.down()
sq()
t.end_fill()
done()

