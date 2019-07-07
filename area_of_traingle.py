from math import *
#a,b,c= 20,85,86

a=int(input("enter first side"))
b=int(input("enter Second side"))
c=int(input("enter third side"))


s= (a+b+c)/2
print("S=",s)

area= sqrt(s*(s-a)*(s-b)*(s-c))

print("area=",area)