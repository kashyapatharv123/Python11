'''def add(x,y):    # here x,y are called formal argumnet
    c=x+y
    print("Sum=",c)

add(55,66)


def add1(x,y,z):    # here x,y are called formal argumnet
    c=x+y+z
    print("Sum=",c)

add1(55,66,8) '''


def dostzod(*b):
#def dostzod(a,*b):
    #c=a
    c=0
    #print(c)
    #print(b)
    for i in b:
        c=c+i
    print(c)




dostzod(55,5,6,44,666)
dostzod(55,66)
dostzod(1,2,3,4,56,6,8,9,999,89,8)