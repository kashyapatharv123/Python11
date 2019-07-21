
from tkinter import *
def msg0():
    print("0")
def msg1():
    print("1")
def msg2():
    print("2")
def msg3():
    print("3")
def msg4():
    print("4")
def msg5():
    print("5")
def msg6():
    print("6")

def msg7():
    print("7")
def msg8():
    print("8")

def msg9():
    print("9")

def msg10():
    print(".")
def msg11():
    print("+")
def msg12():
    print("-")
def msg13():
    print("*")
def msg14():
    print("/")
def msg15():
    print("C")
def msg16():
    print("CE")
def msg17():
    print("%")


root=Tk()
root.title("My Calculator")
root.geometry("300x360+500+200")
#root.resizable(0,0)

display=Entry(root,bd=15,justify="right",font=("Ariel",12),width=25,foreground= "brown",background="yellow"  )
display.grid(row=0,columnspan=4)

btn7=Button(root,text="7",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg7).grid(row=1,column=0)

btn8=Button(root,text="8",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg8).grid(row=1,column=1)

btn9=Button(root,text="9",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg9).grid(row=1,column=2)

btn_mul=Button(root,text="*",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg13).grid(row=1,column=3)

btn4=Button(root,text="4",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg4).grid(row=2,column=0)

btn5=Button(root,text="5",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg5).grid(row=2,column=1)

btn6=Button(root,text="6",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg6).grid(row=2,column=2)

btn_sub=Button(root,text="-",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg12).grid(row=2,column=3)

btn1=Button(root,text="1",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg1).grid(row=3,column=0)

btn2=Button(root,text="2",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg2).grid(row=3,column=1)

btn3=Button(root,text="3",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg3).grid(row=3,column=2)

btn_add=Button(root,text="+",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg11).grid(row=3,column=3)

btn_zero=Button(root,text="0",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg0).grid(row=4,column=0)

btn_dot=Button(root,text=".",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg10).grid(row=4,column=1)

btn_equal=Button(root,text="=",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg10).grid(row=4,column=2)

btn_clear=Button(root,text="CE",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg16).grid(row=4,column=3)

btn_clear1=Button(root,text="C",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg15).grid(row=5,column=0)

btn_cl=Button(root,text=u"\u232B",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg15).grid(row=5,column=1)

btn_div=Button(root,text=u"\u00F7",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg14).grid(row=5,column=2)

btn_per=Button(root,text="%",font=("Ariel",12),bd=15,height=1,width=4,fg="red",bg="blue",command=msg17).grid(row=5,column=3)

mainloop()
