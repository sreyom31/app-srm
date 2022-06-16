from pyDatalog import pyDatalog
pyDatalog.create_terms("N,Factorial")
Factorial[N]=N*Factorial[N-1]
Factorial[1]=1
print(Factorial[4]==N)