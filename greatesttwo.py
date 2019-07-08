a = int(input("Enter first number"))
b = int(input("Enter Second number"))
c = int(input("Enter Third number"))

if a>b:
    if a>c:
        print("A is greatest")
    else:
        print("C is greatest")
elif b>c:
    print("B is greatest")
else:
    print("C is greatest")

