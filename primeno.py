from math import *
'''

5%2  not prime
5%3    not prime
5%4    not prime


10 %2 == 0 prime

'''

num = int(input("enter any number"))
print(num)
'''
i=2
while i<=num-1:
    if num%i==0:
        print("not Prime no")
        break
    else:
        print("Prime")
        break


    i=i+1
'''

'''
i=2
while i<=num-1:
    if num%i==0:
        print("not Prime no")
        break
    i=i+1

else:
    print("prime")
'''

i=2
while i<=sqrt(num):
    if num%i==0:
        print("not Prime no")
        break
    i=i+1

else:
    print("prime")
