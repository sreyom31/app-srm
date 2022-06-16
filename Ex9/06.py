from sympy import *
import sympy as sym
x = sym.Symbol('x')
print(sym.diff(sym.sin(x), x))
print(sym.diff(sym.cos(x), x))
print(sym.diff(sym.log(x), x))
print(sym.diff(x**-1, x))
