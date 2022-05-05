from tkinter import *
root=Tk()

root.geometry=('500x500')
root.title('Flyer')
label_0=Label(root, text='Bookingid')
label_0.grid(row=1,column=1)
entry_1=Entry(root)
entry_1.grid(row=1,column=2)

label_1=Label(root, text='Passenger Name:')
label_1.grid(row=2,column=1)
entry_2=Entry(root)
entry_2.grid(row=2,column=2)

label_2=Label(root, text='Flight')
label_2.grid(row=3,column=1)
entry_3=Entry(root)
entry_3.grid(row=3,column=2)

var=IntVar()
label_3=Label(root, text='Source')
label_3.grid(row=4,column=1)
rb1=Radiobutton(root,text='Delhi',variable=var,value=1)
rb1.grid(row=4,column=2)
rb2=Radiobutton(root,text='Mumbai',variable=var,value=2)
rb2.grid(row=4,column=3)
rb1=Radiobutton(root,text='Chennai',variable=var,value=1)
rb1.grid(row=4,column=4)
rb2=Radiobutton(root,text='Kolkata',variable=var,value=2)
rb2.grid(row=4,column=5)

label_4=Label(root, text='Duration')
label_4.grid(row=5,column=1)
entry_5=Spinbox(root, from_=1, to=80)
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