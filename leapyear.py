a = int(input("Enter  Year"))
print(a)
if a%100==0:
    if a%400==0:
        print("Year is leap")
    else:
        print("Not leap")
elif a%4==0:
    print("Year is leap")
else:
    print("Not leap")



