from sympy import *
import sympy as sym
a = sym.Rational(1,2)
b = sym.Rational(1,3)
print(a+b)

# # 03
# x = sym.Symbol('x')
# y = sym.Symbol('y')
# print(sym.expand((x + y) ** 6))

# # 04
# x = sym.Symbol('x')
# print(sym.simplify(sym.sin(x)/sym.cos(x)))

# # 05
# x = sym.Symbol('x')
# print(sym.limit((sym.sin(x)-x) / x**3,x, 0))

# # 06
# x = sym.Symbol('x')
# print(sym.diff(sym.sin(x), x))
# print(sym.diff(sym.cos(x), x))
# print(sym.diff(sym.log(x), x))
# print(sym.diff(x**-1, x))

# # 07
# x = sym.Symbol('x')
# y = sym.Symbol('y')
# solution = sym.solve((x +y-2,2*x+y), (x, y))
# print(solution[x],solution[y])

# # 08
# x = sym.Symbol('x')
# y = sym.Symbol('y')
# print(sym.integrate(x**2,x))
# print(sym.integrate(sym.sin(x),x))
# print(sym.integrate(sym.cos(x),x))
# print(sym.integrate(x**2,y))
# print(sym.integrate(sym.sin(x),y))
# print(sym.integrate(sym.cos(x),y))

# # 09
# x = sym.Symbol('x')
# f= sym.Function('f')(x)
# a=sym.dsolve(f.diff(x,x)+9*f+1,f)
# print(a)

# 10
# x = sym.Symbol('x')
# y = sym.Symbol('y')
# z = sym.Symbol('z')
# M = sym.Matrix(((3, 7, -12, 0), (4, -2, -5, 0)))
# system = A, b = M[:, :-1], M[:, -1]
# print(sym.linsolve(system, x, y, z))

