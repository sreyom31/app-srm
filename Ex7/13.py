# Write a python program to calculate factorial of given number ( use reduce function)

import functools
num = int(input('Enter a number: '))
def mult(x,y):
    print("x=",x," y=",y)
    return x*y
 
fact=functools.reduce(mult, range(1, num+1))
print ('Factorial of 3: ', fact)