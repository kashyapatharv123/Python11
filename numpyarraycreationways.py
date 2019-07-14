from numpy import *
'''
there are 6 ways to create an array using numpy
1. array()
2. linspace()
3.  logspace()
4. arange()
5. zeros()
6. ones()


'''
arr =linspace(1,50,15)
print(arr)


arr1=logspace(1,15,15)
print(arr1)


arr3=arange(1,15,2)
print(arr3)

arr4=zeros(10)
print(arr4)

arr5=ones(11,int)
print(arr5)