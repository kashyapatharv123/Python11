import time
for i in range(10):
    print(i,end="")
print()
for k in range(2,21):
    print("\t",k,end="")

print()
for k in range(2,21,3):
    print("\t",k,end="")

print()
for k in range(100,90,-1):
    print("\t",k,end="")

print()
l=[2,"fdfd",66.8,66,69,458]
print(l)

for i in range(len(l)):
    time.sleep(1)
    print(l[i])

a=1
b=101
for i in range(a,b):
    if i%2==0:
        print("Even=",i)
    else:
        print("Odd=",i)

num=8
f=1
for i in range(1,num+1):
    f=f*i

print("fact=",f)