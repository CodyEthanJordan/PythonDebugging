# Cody Jordan
# Introduction to Numerical Computing
# Debugging

# PDB documentation
# https://docs.python.org/3/library/pdb.html

import numpy as np

# does this file run?
# Test Early Test Often

name = "foo"
x = np.linspace(0,2*np.pi)

# double click next to line numbe to put breakpoint here
# instead of hitting run hit Debug (Ctrl + F5)
y = np.sin(x)

# QUESTION: how can we make a 2d column array with x and y?
# IPython, test it in interactive mode

# in pdb we can print values with "p", such as "p x"
# why won't p y work?
# Put in w to see where we are in code

def foo():
    variable = 6
    variable2 = 7
    return variable
    
output = foo()


def fibonacci(n):
    if(n == 0):
        return 0
    else:
        return n + fibonacci(n)
        
fib = fibonacci(5)
print(fib)

# use "s" to enter function
# "r" to return from function

def squareTotal(a):
    '''Calculates the sum of the squares of an array'''
    for i in len(a):
        a[i] = a[i]**2

    total = 0
    for i in len(a):
        total = total + a[i]

    return total
    
# how

print(squareTotal(x))