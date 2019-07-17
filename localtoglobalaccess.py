x=80 #global varable
y=8
def msg():
    x=8 #local varable
    print(x)
    p=globals()['x']
    print(p)


msg()
print(x)