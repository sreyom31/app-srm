# Write a Python program to add two given lists and find the difference between lists. Use map() function.

a = input("Enter list elements: ")
seq  = list(map(int,list(a.split())))
result = filter(lambda x: x>=18, seq)
print(list(result))