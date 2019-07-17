def fact(g):
    if g==0:
        return 1
    else:
        return g*fact(g-1)

x = int(input("enter any number"))
print(x)

g=fact(x)
print("factorial=",g)