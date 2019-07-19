from turtle import *
l=["red","green","blue","orange","yellow"]
t=Turtle()
wn=Screen()
wn.title("My turtle")

t.shape("turtle")
t.color("green","red")
t.speed(1)
t.up()
t.goto(200,0)
t.down()
t.pensize(10)
for i in range(5):
    t.pencolor(l[i])
    t.circle(50)
    t.up()
    t.bk(100)
    t.down()



done()