# Write a Python program to calculate sum of numbers from the list and maximum element from the list (use reduce function)

import functools
def mult(x,y):
    return x*y
a=int(input('Enter number to find factorial of:'))
fact=functools.reduce(mult, range(1, a+1))
print ('Factorial: ',fact)