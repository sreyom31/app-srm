from tkinter import *
root=Tk()

root.geometry=('500x500')
root.title('Customer Loan Details')
label_0=Label(root, text='Annual Rate:')
label_0.grid(row=1,column=1)
entry_1=Entry(root)
entry_1.grid(row=1,column=2)

label_1=Label(root, text='Number of Payments:')
label_1.grid(row=2,column=1)
entry_2=Entry(root)
entry_2.grid(row=2,column=2)

label_2=Label(root, text='Loan Principle:')
label_2.grid(row=3,column=1)
entry_3=Entry(root)
entry_3.grid(row=3,column=2)

label_2=Label(root, text='Monthly Payment:')
label_2.grid(row=4,column=1)
entry_3=Entry(root)
entry_3.grid(row=4,column=2)

label_2=Label(root, text='Remaining Loan:')
label_2.grid(row=5,column=1)
entry_3=Entry(root)
entry_3.grid(row=5,column=2)


b1=Button(root, text='Final Balance')
b1.grid(row=6,column=1)

b1=Button(root, text='Monthly Payment')
b1.grid(row=6,column=2)

b1=Button(root, text='Quit')
b1.grid(row=6,column=3)

root.mainloop()