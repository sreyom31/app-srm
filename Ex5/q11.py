import tkinter as tk
from tkinter import *
root = tk.Tk()
root.geometry("310x300")
root.title('Billing')
l1 = tk.Label(root,text = " Name: ").grid(row=0)
t1=tk.Entry(root,width=30).grid(row=0,column=1)
l2 = tk.Label(root,text = " Products: ").grid(row=2)
t2=tk.Entry(root,width=30).grid(row=2,column=1,padx=10,pady=10,ipady=20)
l3 = tk.Label(root,text = " Quantity: ").grid(row=3)
t3=tk.Entry(root,width=30).grid(row=3,column=1)
w = Button(root,width=25, text = " Add Items ",command = root.destroy).grid(row=4,column=1)

e=tk.Entry(root,width=16).place(x=15,y=150, width=250,height=100)


w1 = Button(root,width=15, text = " Clear items ",command = root.destroy).place(x=15,y=260)
w2 = Button(root,width=15, text = " Total ",command = root.destroy).place(x=150,y=260)

root.mainloop()
