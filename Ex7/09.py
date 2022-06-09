# Filter the array, and return a new array with only the values equal to or above 18 ( consider filter function)

a = input("Enter list elements: ")
seq  = list(map(int,list(a.split())))
result = filter(lambda x: x>=18, seq)
print(list(result))