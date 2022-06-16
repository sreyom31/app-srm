from sympy import *
import sympy as sym
x = sym.Symbol('x')
y = sym.Symbol('y')
print(sym.integrate(x**2,x))
print(sym.integrate(sym.sin(x),x))
print(sym.integrate(sym.cos(x),x))
print(sym.integrate(x**2,y))
print(sym.integrate(sym.sin(x),y))
print(sym.integrate(sym.cos(x),y))