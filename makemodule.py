def add(*a):
    c=0
    for i in a:
        c=c+i
    print(c)


def multi(*a):
    c=1
    for i in a:
        c=c*i
    print(c)


f=lambda x,y:x+y


print("makemodule=",__name__)

if __name__=="__main__" :
    def msg():
        print("Made by techsrijan")

    msg()
else:
    print(":module not accessble")

