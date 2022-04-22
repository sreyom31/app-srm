from tkinter import *

def clickDispay(value):
    Label(root, text=value).grid(row=7, column=1)

root = Tk()
root.title('Student Registration Form')
root.geometry('500x500')

Label(root, text="RegnNo: ").grid(row=0, column=0)
Entry(root).grid(row=0, column=1)
Label(root, text="Name: ").grid(row=1, column=0)
Entry(root).grid(row=1, column=1)
Label(root, text="Dept: ").grid(row=2, column=0)
Entry(root).grid(row=2, column=1)

a = IntVar()
Label(root, text="Gender").grid(row=3, column=0)
Radiobutton(root, value=0, variable=a, text='Male').grid(row=3, column=1)
Radiobutton(root, value=1, variable=a, text='Female').grid(row=3, column=2)

Label(root, text='age').grid(row=4, column=0)
Spinbox(root, from_=18, to=28).grid(row=4, column=1)
b1 = Button(root, text='Insert', command=lambda: clickDispay('Insert')).grid(row=5, column=0)
b2 = Button(root, text='Update', command=lambda: clickDispay('Update')).grid(row=5, column=1)

b3 = Button(root, text='Delete', command=lambda: clickDispay('Delete')).grid(row=6, column=0)
b4 = Button(root, text='Select', command=lambda: clickDispay('Select')).grid(row=6, column=1)

label = Label(root, textvariable=" ").grid(row=7, column=1)


root.mainloop()