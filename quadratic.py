from math import *
a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
c = int(input("Enter the value of c"))


d= b*b-4*a*c

if d==0:
    print("roots are equal")
    x1=-b/(2*a)
    x2=x1
    print("X1=",x1,"X2=",x2)
elif d>0:
    print("roots are unequal")
    x1 = (-b+sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    print("X1=", x1, "X2=", x2)

else:
    print("roots are imaginary")



