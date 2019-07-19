from turtle import *

t=Turtle()
wn=Screen()
wn.title("My turtle")

t.shape("turtle")
t.color("green","red")
t.speed(1)
t.circle(100,steps=5)
t.goto(300,0)
t.circle(100,extent=45)
#t.circle(-100)
done()
