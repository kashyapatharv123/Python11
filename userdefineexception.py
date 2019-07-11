try:
    age = int(input("enter your age"))
    if age<0:
        raise ValueError
    else:
        print("age=",age)


except ValueError:
    print("Pagla gaye ho ka age kahi negative hota hi")


print("\U0001F601")
print(u"\u0906\u092E")