# Write a Python program to create Fibonacci series upto n using Lambda.

from functools import reduce
  
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                 range(n-2), [0, 1])
a=int(input('Enter no. of elements:'))
print(fib(a))