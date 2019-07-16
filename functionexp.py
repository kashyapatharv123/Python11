#print("good morning")


#function definition
'''def greet():
    print("good morning")

#function call
greet()
greet()


def add(x,y):    # here x,y are called formal argumnet
    c=x+y
    print("Sum=",c)

a= int(input("enter first no"))
b= int(input("enter second no"))

#function call
add(a,b)   #here a,b are called atual argument

add(100,200)

greet()
x= int(input("enter first no"))
y= int(input("enter second no"))
add(x,y)   #here a,b are called atual argument
'''

def multi(x,y):
    res=x*y
    return res


k=multi(5,6)
print(k)

def calc(p,q):
    x=p*q
    y=p+q
    return x,y

# a,b=5,6
g,h=calc(100,200)
print(g)
print(h)

def msg():
    return "hello"

print(msg())