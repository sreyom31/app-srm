# Write a Python program to sort a given list of strings(numbers) numerically using lambda.

def sort_n(nums_str):
    result = sorted(nums_str, key=lambda el: int(el))
    return result
a = input("Enter list elements separated by space: ")
l1 = list(map(int,list(a.split())))
print("Original list:")
print(l1)
print("\nSorted:")
print(sort_n(l1))