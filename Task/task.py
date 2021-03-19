from tkinter import *
from tkvideo import tkvideo

btn1count = 0
btn2count = 0
btn3count = 0
btn4count = 0

def clickbtn1():
    label1.config(bg='yellow',text="Button 1 Clicked!!!")
    global btn1count 
    btn1count +=1
    if btn1count%2==0:
        label1.config(bg="gray95",text="label1")
 

def clickbtn2():
    label2.config(bg='red',text="Button 2 Clicked!!!")
    global btn2count 
    btn2count +=1
    if btn2count%2==0:
        label2.config(bg="gray95",text="label2")

def clickbtn3():
    label3.config(bg='orange',text="Button 3 Clicked!!!")
    global btn3count 
    btn3count +=1
    if btn3count%2==0:
        label3.config(bg="gray95",text="label3")

def clickbtn4():
    label4.config(bg='green',text="Button 4 Clicked!!!")
    global btn4count 
    btn4count +=1
    if btn4count%2==0:
        label4.config(bg="gray95",text="label3")

root = Tk()
my_label = Label(root)
my_label.place(x=10,y=10)
player = tkvideo("Earth.mp4", my_label, loop = 1,size=(300,300))
player.play()

label1 = Label(root,text="Label 1")
label2 = Label(root, text="Label 2")
label3 = Label(root, text="Label 3")
label4 = Label(root, text="Label 4")

btn1 = Button(root,text="1", command=clickbtn1)
btn2 = Button(root,text="2",command=clickbtn2)
btn3 = Button(root,text="3",command=clickbtn3)
btn4 = Button(root,text="4",command=clickbtn4)

label1.place(x=330 , y=10)
label2.place(x=330 , y=80)
label3.place(x=330 , y=160)
label4.place(x=330 , y=240)

btn1.place(width=50, x=20 , y=430)
btn2.place(width=50, x=120 , y=430)
btn3.place(width=50, x=220 , y=430)
btn4.place(width=50, x=320 , y=430)
root.geometry("500x500+120+120")
root.mainloop()