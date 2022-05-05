from tkinter import *
root = Tk()
root.geometry("400x300")
title = Label(root, text="Welcome to Real Time Currency Converter",
              width=40, justify=CENTER)
title.config(background="light blue", pady=2, padx=2)
title.grid(row=0, column=0, columnspan=2)
money = Label(root, text="1 USD = 75.00 Indian Rupee\nDate:2022-05-22",
              font=("bold", 13))
money.grid(row=2, column=0, pady=5, columnspan=2)
option = StringVar()
option.set("USD")
option2 = StringVar()
option2.set("INR")
options = ["USD", "INR", "EURO", "POUND"]
currencySelect = OptionMenu(root, option, *options)
currencySelect.grid(row=4, column=0)
moneyEntry = Entry(root, bd=1)
moneyEntry.grid(row=5, column=0)
currencySelect2 = OptionMenu(root, option2, *options)
currencySelect2.grid(row=4, column=1)
moneyEntry2 = Label(root, bg="white", width=16, bd=1)
moneyEntry2.grid(row=5, column=1)


def convert():
    fromCurr = option.get()
    toCurr = option2.get()
    print(fromCurr, toCurr)
    if fromCurr == "USD":
        if toCurr == "USD":
            moneyEntry2.config(text=str(float(moneyEntry.get()) * 1))
        elif toCurr == "INR":
            moneyEntry2.config(text=str(float(moneyEntry.get()) * 75.00))
        elif toCurr == "EURO":
            moneyEntry2.config(text=str(float(moneyEntry.get())*0.93))
        elif toCurr == "POUND":
            moneyEntry2.config(text=str(float(moneyEntry.get())*0.78))
    elif fromCurr == "INR":
        if toCurr == "USD":
            moneyEntry2.config(text=str(float(moneyEntry.get()) * 0.013))
        elif toCurr == "INR":
            moneyEntry2.config(text=str(float(moneyEntry.get()) * 1))
        elif toCurr == "EURO":
            moneyEntry2.config(text=str(float(moneyEntry.get()) * 0.012))
        elif toCurr == "POUND":
            moneyEntry2.config(text=str(float(moneyEntry.get()) * 0.010))
    elif fromCurr == "POUND":
        if toCurr == "USD":
            moneyEntry2.config(text=str(float(moneyEntry.get()) * 1.28))
        elif toCurr == "INR":
            moneyEntry2.config(text=str(float(moneyEntry.get()) * 98.19))
        elif toCurr == "EURO":
            moneyEntry2.config(text=str(float(moneyEntry.get()) * 1.19))
        elif toCurr == "POUND":
            moneyEntry2.config(text=str(float(moneyEntry.get()) * 1))
    elif fromCurr == "EURO":
        if toCurr == "USD":
            moneyEntry2.config(text=str(float(moneyEntry.get()) * 1.08))
        elif toCurr == "INR":
            moneyEntry2.config(text=str(float(moneyEntry.get()) * 82.74))
        elif toCurr == "EURO":
            moneyEntry2.config(text=str(float(moneyEntry.get()) * 1))
        elif toCurr == "POUND":
            moneyEntry2.config(text=str(float(moneyEntry.get()) * 0.84))


button = Button(root, text="Convert", fg="white", bg="Blue",
                command=convert)
button.grid(row=6, columnspan=2, pady=10)
root.mainloop()
