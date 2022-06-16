from sympy import *
import sympy as sym
x = sym.Symbol('x')
f= sym.Function('f')(x)
a=sym.dsolve(f.diff(x,x)+9*f+1,f)
print(a)

