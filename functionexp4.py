
# 5. keyword variable length
def persondata(name,**data):
    print(name)
    print(data)
    for i ,j in data.items():
        print(i,j)


persondata(name="bcd",age=16,city="gkp",phone=9956477467,roll=5)
