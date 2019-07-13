num=int(input("enter any number"))
orig=num
sum1=0
while num>0:
    a=num%10
    sum1= sum1+a*a*a
    num=num//10

print(sum1)
if sum1==orig:
    print("armstrong")
else:
    print("not arm strong")