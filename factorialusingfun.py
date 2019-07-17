def fact(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f


x = int(input("enter any number"))
print(x)

g=fact(x)
print("factorial=",g)