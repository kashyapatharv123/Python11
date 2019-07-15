from numpy import *
arr=array([1,2,3,4,56])
print(arr)
print("arr id=",id(arr))

#aliasing
arr2=arr
print(arr2)
print("arr2 id=",id(arr2))

#what if u want differnt address
#shallow copy
arr3=arr.view()
print(arr3)
print("arr3 id=",id(arr3))

arr[1]=5000
print(arr)
print(arr2)
print(arr3)

#what if u want differnt address and changes does not effect each other
#deep copy
print("arr4")
arr4=arr.copy()
print(arr4)
print("arr4 id=",id(arr4))

arr[0]=666
print(arr)
print(arr4)
