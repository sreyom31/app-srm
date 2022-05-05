from tkinter import *
root = Tk()
Lname = StringVar()
lname, fname = StringVar(), StringVar()
email = StringVar()
bday = StringVar()
Label(root, text="Contact List", width=25, justify=CENTER).grid(row=0,
                                                                column=0)
contactList = Listbox(root, width=25, height=8).grid(row=1, column=0,
                                                     rowspan=4)
Button(root, text="Display Contact", width=20, height=1,
       justify=CENTER).grid(row=5, column=0, pady=8)
name = Label(root, text="Last Name ", width=15, justify=LEFT).grid(row=6,
                                                                   column=0)
Entry(root, textvariable=Lname, width=25).grid(row=6, column=1)
search = Button(root, text="Search", width=15, justify=CENTER).grid(row=7,
                                                                    column=1, pady=15)
Label(root, text="New Contact : ", width=25, justify=CENTER).grid(row=0,
                                                                  column=2, padx=8)
fn = Label(root, text="First Name : ", width=15, justify=LEFT,
           anchor="e").grid(row=1, column=2, padx=8)
Entry(root, textvariable=fname, width=25).grid(row=1, column=3)
ln = Label(root, text="Last Name : ", width=15, justify=LEFT,
           anchor="e").grid(row=2, column=2, padx=8)
Entry(root, textvariable=lname, width=25).grid(row=2, column=3)
phn = Label(root, text="Phone # : ", width=15, justify=LEFT,
            anchor="e").grid(row=3, column=2, padx=8)
Entry(root, textvariable=phn, width=25).grid(row=3, column=3)
emailEl = Label(root, text="Email : ", width=15, justify=LEFT,
                anchor="e").grid(row=4, column=2, padx=8)
Entry(root, textvariable=email, width=25).grid(row=4, column=3)
bdayEl = Label(root, text="Birthday : ", width=15, justify=LEFT,
               anchor="e").grid(row=5, column=2, padx=8)
Entry(root, textvariable=bday, width=25).grid(row=5, column=3)
Button(root, text="Add Contact", width=15, justify=RIGHT).grid(row=6,
                                                               column=3, sticky="e")
Label(root, text="Result:\nLast, First\nPhone").grid(row=8, column=3,
                                                     sticky="sw")
root.mainloop()
