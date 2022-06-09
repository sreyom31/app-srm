# Write a Python program to filter only vowels from given sequence.

from functools import reduce
a = input("Enter list elements: ")
scores = list(map(int,list(a.split())))
total = reduce(lambda a, b: a + b, scores)
print(total,max(scores))