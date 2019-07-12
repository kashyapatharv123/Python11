f=1
s=2
noofterms = int(input("enter the no terms u want"))
print(f,",\t",s,end=",")
i=1
while i<=noofterms:
    t=f+s
    print("\t",t,end=",")
    f=s
    s=t
    i=i+1

'''
armstrong no
153=1*1*1+5*5*5+3*3*3=153
magic no
123=1+2+3=6
123=1*2*3=6
palindrome no
121=121

'''