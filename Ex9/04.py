from sympy import *
import sympy as sym
x = sym.Symbol('x')
print(sym.simplify(sym.sin(x)/sym.cos(x)))