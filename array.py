from array import  *


marks1=array('i',[4,5,6,3,23,55,55])
print(marks1)


marks2=array('f',[4,5,6,3,23,55,55])
print(marks2)

for i in marks2:
    print(i)

for k in range(len(marks2)):
    print(marks2[k])

print(marks2[3])

print(marks2.buffer_info())

print(marks2.typecode)

print(marks1.typecode)

j=0
while j<(len(marks2)):
    print(marks2[j])
    j=j+1


