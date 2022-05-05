from tkinter import *
root=Tk()

root.geometry=('500x500')
root.title('Movie Booking Ticket')
label_0=Label(root, text='Movie Booking id')
label_0.grid(row=1,column=1)
entry_1=Entry(root)
entry_1.grid(row=1,column=2)

label_1=Label(root, text='Person Name:')
label_1.grid(row=2,column=1)
entry_2=Entry(root)
entry_2.grid(row=2,column=2)

label_2=Label(root, text='Movie Name')
label_2.grid(row=3,column=1)
entry_3=Entry(root)
entry_3.grid(row=3,column=2)

var=IntVar()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
label_3=Label(root, text='Class')
label_3.grid(row=4,column=1)
rb1=Radiobutton(root,text='A',variable=var,value=1)
rb1.grid(row=4,column=2)
rb2=Radiobutton(root,text='B',variable=var,value=2)
rb2.grid(row=4,column=3)
label_3_1=Label(root, text='Time of Show')
label_3_1.grid(row=4,column=4)
rb1=Checkbutton(root,text='7.15 pm',variable=CheckVar1, onvalue=1, offvalue=0)
rb1.grid(row=4,column=5)
rb2=Checkbutton(root,text='9 am',variable=CheckVar2, onvalue=1, offvalue=0)
rb2.grid(row=4,column=6)

label_4=Label(root, text='Duration')
label_4.grid(row=5,column=1)
entry_5=Scale(root, from_=3, to=100, orient='horizontal')
entry_5.grid(row=5,column=2)

b1=Button(root, text='Insert')
b1.grid(row=6,column=1)

b1=Button(root, text='Update')
b1.grid(row=6,column=2)

b1=Button(root, text='Delete')
b1.grid(row=7,column=1)

b1=Button(root, text='Select')
b1.grid(row=7,column=2)

root.mainloop()