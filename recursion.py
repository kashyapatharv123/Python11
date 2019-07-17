from sys import *
print(getrecursionlimit())
setrecursionlimit(2000)
print(getrecursionlimit())
# when a function call itself it is called recursion
i=0
def msg():
    global i
    print(i,"good afternoon")
    i=i+1
    msg()

msg()
