from turtle import *

t=Turtle()
wn=Screen()
wn.title("My turtle")
#wn.bgcolor("yellow")
#wn.bgpic("test.gif")
t.shape("turtle")
t.color("green","red")
t.speed(1)
t.pensize(10)
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)

t.end_fill()
done()


