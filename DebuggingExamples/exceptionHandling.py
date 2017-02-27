# Cody Jordan
# Introduction to Numerical Computing
# Debugging

# Some good documentation at
# https://docs.python.org/3/tutorial/errors.html

# what do we do if our code makes an error?

x = int(input("Please enter a number: "))

# if we don't put in a number we get an error, read the stack trace

# Usually if we have an error we want to fix it, but sometimes we need to make
# a program which deals with things outside our control

try:
    x = int(input("Please enter a number: "))    
except ValueError:
    print('Thats not a number!')
    x = None
    

