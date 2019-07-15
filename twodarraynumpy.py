from numpy import *
arr=array([

    [1,2,3],
    [2,5,6],


])

print(arr)
print(arr.dtype)
print(arr.shape)
print(arr.size)
arr2=arr.flatten()
print(arr2)

arr3=arr2.reshape(3,2)
print(arr3)