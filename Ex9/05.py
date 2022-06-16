from sympy import *
import sympy as sym
x = sym.Symbol('x')
print(sym.limit((sym.sin(x)-x) / x**3,x, 0))