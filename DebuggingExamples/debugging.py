#!/usr/bin/env python3
# Cody Jordan
# Introduction to Numerical Computing
# Debugging

# PDB documentation
# https://docs.python.org/3/library/pdb.html

import numpy as np

# Put a breakpoint next to y = np.sin(x) by double clicking next to the line number
# Hit Debug file (the blue arrow at the top, or ctrl+F5) to start pdb

# enter 'l' to see what code is around us
# enter 'c' to continue to the next breakpoint

name = "foo"
x = np.linspace(0,2*np.pi)
# put in 'p x' and 'p y' to print the values of x and y
y = np.sin(x)
# QUESTION: why won't p y do anything?
# press 'n' to go to next line
# we can also press enter to repeat the last command, lets use that to
# get down to just after the statement xAndY = x + y

# QUESTION: how can we make a 2d column array with x and y?
xAndY = x + y # this isn't quite right...
# IPython, test it in interactive mode
# Stop debugging, edit the file, turn back on the debugger
# the second time through try 'p y', why does it work?
# We can clear out these local variables by restarting our python console
# To do this in spider close it, right click, and open a new console

def foo():
    variable = 6
    variable2 = 7
    return variable
    
# if we use n we won't be able to see inside the function, how can we look at 
# what goes on inside foo()?    
output = foo()
# either put a breakpoint in foo, or use 's' to step in to the function


def fibonacci(n):
    if(n == 0): # we can hit 'w' to see a stack trace of where we are
        return 0
    else:
        return n + fibonacci(n)
        
fib = fibonacci(5) # QUESTION: error message! what went wrong?
print(fib)


# QUESETION: what does this function do?
# QUESTION: what do you think the programmer meant to do?
def squareTotal(a):
    '''Calculates the sum of the squares of an array'''
    for i in len(a):
        a[i] = a[i]**2

    total = 0
    for i in len(a):
        total = total + a[i]

    return total
    

print(squareTotal(x))
print(x)
# QUESTION: is there a way to improve squareTotal?
#