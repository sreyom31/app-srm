# Write a Python program to add two given lists and find the difference between lists. Use map() function.

def add_sub(x, y):
    return x + y, x - y
 
a = input("Enter first list elements: ")
nums1 = list(map(int,list(a.split())))
b = input("Enter second list elements: ")
nums2 = list(map(int,list(b.split())))
print("Original lists:")
print(nums1)
print(nums2)
result = map(add_sub, nums1, nums2)
print("\nResult:")
print(list(result))