from numpy import *
arr=array([

    [1,22,3],
    [2,5,6],


])

print(arr)

arr2=array([
    [1,1],
    [2,2],
    [3,3]

])

print(arr2)

a=matrix(arr)
print("matrix a")
print(a)

b=matrix(arr2)
print("matrix b")
print(b)

'''
c=a+b
print("matrix c")
print(c)
'''
'''
(2,3)
(3,2)


(2,3)
(2,3)
'''

d=a*b
print(d)
print("arr4")
arr4=array([
    [1,1,1,1],
    [2,2,2,2],
    [3,3,3,3],
    [4,4,4,4]

])

print(arr4)
print(diagonal(arr4))

print(transpose(arr4))

print(a.min())
print(a.max())

