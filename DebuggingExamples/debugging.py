# Cody Jordan
# Introduction to Numerical Computing
# Debugging

# PDB documentation
# https://docs.python.org/3/library/pdb.html

import numpy as np

name = "foo"
x = np.linspace(0,2*np.pi)

# double click next to line numbe to put breakpoint here
# instead of hitting run hit Debug (Ctrl + F5)
y = np.sin(x)

# in pdb we can print values with "p", such as "p x"
# why won't p y work?
# Put in w to see where we are in code

def fibonacci(n):
    if(n == 0):
        return 0
    else:
        return n + fibonacci(n)
        
fib = fibonacci(5)
print(fib)

# use "s" to enter function

def squareTotal(a):
    '''Calculates the sum of the squares of an array'''
    for i in len(a):
        a[i] = a[i]**2

    total = 0
    for i in len(a):
        total = total + a[i]

    return total
    
print(squareTotal(x))