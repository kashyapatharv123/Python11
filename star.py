from turtle import *
l=["red","green","blue","orange","yellow"]
t=Turtle()
wn=Screen()
wn.title("My turtle")

t.shape("turtle")
t.color("green","red")
t.speed(1)
'''t.fd(200)
t.right(144)
t.fd(200)
t.right(144)
t.fd(200)
t.right(144)
t.fd(200)'''
t.up()
#t.left(45)
#t.forward(100)
t.goto(100,50)
t.down()
for i in range(5):
    t.pencolor(l[i])
    t.pensize(10)
    t.fd(200)
    t.right(144)



done()

