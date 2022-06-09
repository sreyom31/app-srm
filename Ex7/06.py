# Write a Python program to convert a given list of strings into list of lists using map function.

def strings_to_listOflists(str):
    result = map(list, str)
    return list(result)

c = input("Enter list of strings separated by space: ")
colors = c.split()
print('List of strings:')
print(colors)
print("\nList of lists:")
print(strings_to_listOflists(colors))