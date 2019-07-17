
lst=[1,2,3,4,5,6]
def passlist(l):
    even=0
    odd=0
    for i in l:
        if i%2==0:
            even=even+i
        else:
            odd=odd+i

    return even,odd


x,y=passlist(lst)
print(x)
print(y)
print("even:{} and odd:{}".format(x,y))