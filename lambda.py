from functools import *
def add(x,y):
    return (x+y)


print(add(6,7))

'''
takes any no of argument but can have only one line working
anumymous function
'''
f=lambda x,y:x+y

print(f(55,20))

'''
filter map and reduce
'''
'''def is_even(n):
    return n%2==0'''


num=[1,55,44,88,2,99,7,87,100]

#even=list(filter(is_even,num))


even=list(filter(lambda n:n%2==0,num))
print(even)

sq=list(map(lambda n:n*n,even))
print(sq)

total=reduce(lambda a,b:a+b,sq)
print(total)