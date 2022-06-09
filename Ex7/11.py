# Write a Python program to calculate sum of numbers from the list and maximum element from the list (use reduce function)

from functools import reduce
a = input("Enter list elements: ")
scores = list(map(int,list(a.split())))
total = reduce(lambda a, b: a + b, scores)
print(total,max(scores))