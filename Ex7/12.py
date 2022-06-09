# Write a python program to calculate factorial of given number ( use reduce function)

import functools
def mult(x,y):
    return x*y
a=int(input('Enter number to find factorial of:'))
fact=functools.reduce(mult, range(1, a+1))
print ('Factorial: ',fact)