num = int(input("how many candy u want"))
av=10

i=1
while i<=num:
    if i<=av:
        print("Please Collect candy:",i)
    else:
        print("Out Of stock")
        break
    i=i+1
else:   # this else will run when the loop properly runs
    print("Thank u please visit again")
