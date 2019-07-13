from array import  *

n= int(input("no of students u have"))

arr=array('i',[])
for i in range(n):
    x=int(input("enter the marks of studnet"))
    arr.append(x)


print(arr)