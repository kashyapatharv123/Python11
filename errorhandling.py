'''
Error(bug)
1. Syntax Error(Compile time error)
2. Logical Error (Human error)
3.Run Time Error(Exception)

'''

'''

a = int(input("enter first number"))

b = int(input("enter Second  number"))

if b==0:
    print("B can not be zero")
else:
    c = a/b
    print(c)


print("thank you")'''


try:
    print("freez open")
    #risky code
    a = int(input("enter first number"))

    b = int(input("enter Second  number"))

    c = a/b
    print(c)


except ZeroDivisionError as e:
    print("b can not be zero:",e)


except ValueError as e:
    print("you have not entered a digit:",e)


except Exception as e:
    print("something went wrong:",e)


finally:
    #always executes
    print("freez closed")
    print("thanks")