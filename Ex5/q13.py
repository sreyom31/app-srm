from tkinter import ttk
from tkinter import *
root = Tk()
phone_list = ttk.Style()
tree = ttk.Treeview(root, column=("ID", "Title", "Author", "Year", "ISBN"),
                    show='headings', height=7)
id = 3
tree.column("#1", anchor=CENTER)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Title")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Author")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="Year")
tree.column("# 5", anchor=CENTER)
tree.heading("# 5", text="ISBN")


def add():
    global id
    tree.insert('', 'end', values=(id, title.get(), auth.get(), year.get(),
                                   isbn.get()))
    title.delete(0, END)
    auth.delete(0, END)
    year.delete(0, END)
    isbn.delete(0, END)
    id += 1


def delete():
    global id
    selected_item = tree.selection()[0]
    tree.delete(selected_item)
    id -= 1


def edit():
    selected_item = tree.selection()[0]
    tree.item(selected_item, values=(id, title.get(), auth.get(),
                                     year.get(), isbn.get()))


Label(root, text="Title").grid(row=0, column=0)
title = Entry(root)
title.grid(row=0, column=1)
Label(root, text="Author").grid(row=0, column=2)
auth = Entry(root)
auth.grid(row=0, column=3)
Label(root, text="Year").grid(row=1, column=0, pady=15)
year = Entry(root)
year.grid(row=1, column=1, pady=15)
Label(root, text="ISBN").grid(row=1, column=2, pady=15)
isbn = Entry(root)
isbn.grid(row=1, column=3, pady=15)
scroll_bar = ttk.Scrollbar(root,
                           orient="vertical",
                           command=tree.yview)
scroll_bar.grid(row=2, column=2, sticky="nsew", pady=15, rowspan=6)
tree.configure(yscrollcommand=scroll_bar.set)
tree.insert('', 'end', values=('1', 'The Earth', 'Sreyom', '2020',
                               '4545664551536'))
tree.insert('', 'end', values=('2', 'The Moon', 'Ojas', '2022',
                               '5545446546646'))
tree.grid(row=2, columnspan=2, pady=15, rowspan=6)
Button(root, text="View All", command=edit, width=15,
       justify=CENTER).grid(row=2, column=3)
Button(root, text="Search", command=delete, width=15,
       justify=CENTER).grid(row=3, column=3)
Button(root, text="Add", command=add, width=15, justify=CENTER).grid(row=4,
                                                                     column=3)
Button(root, text="Update Selected", command=edit, width=15,
       justify=CENTER).grid(row=5, column=3)
Button(root, text="Delete Selected", command=delete, width=15,
       justify=CENTER).grid(row=6, column=3)
Button(root, text="Close", command=root.destroy, width=15,
       justify=CENTER).grid(row=7, column=3)
root.mainloop()
