from sympy import *
import sympy as sym
x = sym.Symbol('x')
y = sym.Symbol('y')
solution = sym.solve((x +y-2,2*x+y), (x, y))
print(solution[x],solution[y])