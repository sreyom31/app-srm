from tkinter import *

root = Tk() 
root.geometry("350x310")
root.title('PythonGuides')
root.configure(background="#d1d1c7");
l1 = Label(root,text = "Full Name ",background="#f4f4f3").place(x=50,y=10)
t=Entry(root,width=30).place(x=130,y=10)
l2=Label(root,text="Email ",background="#f4f4f3").place(x=50,y=40)
t=Entry(root,width=30).place(x=130,y=40)
l3=Label(root,text="Password ",background="#f4f4f3").place(x=50,y=65)
t=Entry(root,width=30).place(x=130,y=65)

radio=IntVar()
frame = Frame(root,background="#f4f4f3",bd=5)
frame.place(x=90,y=100)
w = LabelFrame(frame, text='Gender',background="#f4f4f3", relief=GROOVE,padx=60,pady=15)
w.grid(row=4, column=2)

rb1=Radiobutton(w,text='Female',variable=radio,value=1,background="#f4f4f3").grid(row=5,column=1)
rb2=Radiobutton(w,text='Male',variable=radio,value=2,background="#f4f4f3").grid(row=6,column=1)
rb3=Radiobutton(w,text='Others',variable=radio,value=3,background="#f4f4f3").grid(row=7,column=1)

v1=IntVar()
cb1=Checkbutton(root,text='Accept the terms & conditions',variable=v1, onvalue=1,background="#f4f4f3",width=35)
cb1.place(x=40,y=240)
button=Button(root, text='Submit', width=25,background="#f4f4f3").place(x=70,y=270)
root.mainloop()
