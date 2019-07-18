'''l=[3,5,4]
print(l)

#list is a function to create list
l3=list()
print(l3)

l1=list( input("Enter the elemnts of list"))
print(l1)

l3 =eval( input("Enter the elemnts of list"))
print(l3)'''

name,age=input("Enter name and age").split(',')
age=int(age)
print(name,age)

a,b,c,d,e=[int(i)for i in input("enter two no").split()]
print("Number of list is: ",a,b,c,d,e)

