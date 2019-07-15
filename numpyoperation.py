from numpy import *
arr=array([1,2,3,4,56])
print(arr)

print(arr+5)

arr2=ones(5,int)
print(arr2)

arr3=arr+arr2

print(arr3)

print(sqrt(arr))
print(max(arr))
print(sum(arr))
print(min(arr))
print(concatenate([arr,arr2]))

print(concatenate([arr2,arr]))

name = array(['ram','shyam','mohan'])
print(name)
title=array(['sharma','singh','srivastava'])
print(concatenate([name,title]))


nextname=name
print(nextname)