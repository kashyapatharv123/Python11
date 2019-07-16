def person(name,age):
    print("name=",name)
    print("age=",age)


person("ashwani",33)

person(33,"ancd")


def person1(name,age):
    print("name=",name)
    age=age+10
    print("age=",age)
#1. positional argument
person1("ashwani",33)

#person1(33,"ancd")
'''
pass an agument to function
1. positional argument
2. keyword argument
3. default argumnt
4. variable length argument (*)
5. keword variable length argumnent
'''

#2. keyword argument

person1(name="hum",age=40)
person1(age=5,name="gfdg")

def persondata(name,city,age=18,roll=12):
    print("name=",name)
    age=age+10
    print("age=",age)
    print("city=",city)
    print("roll=", roll)

persondata(city="gkp",name="ssss",age=646)

persondata(city="lko",name="534534")