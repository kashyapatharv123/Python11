a=20
if a>25:
    pass
else:
    print("hi")

'''i=1
while i<10:
    if i%3==0:
        pass
    else:
        print(i)
    i=i+1'''

'''i=1
while i<10:
    if i%3==0:
        break
    else:
        print(i)
    i=i+1'''
'''
Python continue statement. It returns the control to the beginning 
of the while loop.. The continue statement rejects all the remaining 
statements in the current
 iteration of the loop and moves the control back to the top of the loop
'''
i=1
while i<10:
    i=i+1
    if i%3==0:
        continue
    else:
        print(i)
    #i=i+1
