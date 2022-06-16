from sympy import *
import sympy as sym
x = sym.Symbol('x')
y = sym.Symbol('y')
z = sym.Symbol('z')
M = sym.Matrix(((3, 7, -12, 0), (4, -2, -5, 0)))
system = A, b = M[:, :-1], M[:, -1]
print(sym.linsolve(system, x, y, z))