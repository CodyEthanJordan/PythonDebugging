# Cody Jordan
# Introduction to Numerical Computing
# Exception Handling


# what do we do if our code makes an error?

x = int(input("Please enter a number: "))

# if we don't put in a number we get an error when we try to force the input
# to be an integer

# Usually if we have an error we want to fix it, but sometimes we need to make
# a program which deals with things outside our control.
# Typically this is because we are accessing user input, the filesystem, the 
# internet, or another real-world entity

try:
    x = int(input("Please enter a number: "))    
except ValueError:
    print('Thats not a number!')
    x = None
    
# Making a function which is able to raise its own exceptions
def CauseException(e):
    '''Tests raising various kinds of exceptions, must pass in an integer or the 
    function raises a TypeException.
    e == 1 raises a NameError
    e == 2 does not raise any error
    all other values raise a ZeroDivisionError'''
    if type(e) != int:
        # we can also raise an exception ourselves
        # in this case our function checks to see if e is actually an integer
        raise TypeError("Type is incorrect, argument to CauseException must be int")
        # in many python functions this is the responsability of the caller to RTFM
        # but we can implement type checking if we want
    elif e == 1:
        # we can also raise any of the Python exceptions that we want, with whatever message we choose
        # the docs have a full list of these
        # https://docs.python.org/3/library/exceptions.html
        raise NameError("Invalid name in CauseException")
    elif e == 2:
        pass #the pass statement does nothing, meaning that when e is 2 we do not raise an exception
        # this statement is useful for being a placeholder in a point in code
        # which it is syntatically incorrect to leave blank, such as after an if:
    else:
        # this statement will raise a ZeroDivisionError
        x = 8 / 0
        print(x)

# Here is the Python documentation on handling errors
# https://docs.python.org/3/tutorial/errors.html
        
try:
    CauseException(1)
    CauseException('hello')
except TypeError as error: 
    # this block of code will be used if anything in the try block raises a TypeError
    # the TypeError is made into a local variable called error
    print("Encountered a TypeError, message: ")
    print(error.args) # this is the message we defined in the funciton
    print("Please see the documentation for CauseException")
    print(CauseException.__doc__) # print the docstring
except NameError:
    # this block will be used if anything in try raises a NameError
    raise # having only the keyword raise will mean that this exception is passed
    # out of the try block and on to the next level of the program, whatever called this section
    # if an exception is passed all the way to the start of the program then it
    # becomes an 'unhandled exception'
    # In this case execution stops, and an error message is printed
except: # this block is used to catch any type of exception at all not previously listed
    print('Some form of exception occured')
else: # the else statement means that no exceptions at all occured in the try block
    print('No exception occured')
finally:
    # the finally block is ALWAYS executed, no matter how badly things went 
    # in the try block. This is used to clean up any loose ends and quit gracefully
    print('Cleaning up')
    

        