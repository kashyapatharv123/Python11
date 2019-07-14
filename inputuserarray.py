from array import  *

n= int(input("no of students u have"))

arr=array('i',[])
for i in range(n):
    x=int(input("enter the marks of studnet"))
    arr.append(x)


print(arr)

search = int(input("enter the marks u want to search"))
for i in  range(len(arr)):
    if search==arr[i]:
        print("item found",i)
        break
else:
    print("item not found")



print(arr.index(search))
print(max(arr))