#!/usr/bin/env python3
# Cody Jordan
# Introduction to Numerical Computing
# Exception Handling

import sys
import logging
import traceback as tb

# with the logging module we can create a logger which will write
log = logging.getLogger('ExceptionLogger') # create a new logger called ExceptionLogger
log.setLevel(logging.INFO) # this log will only keep track of messages which are
# at least of INFO importance and above
# you can see the levels listed here
# https://docs.python.org/3/library/logging.html#logging-levels

fileHandler = logging.FileHandler('ErrorLog.log') 
# when we write to the log our messages will get put in a file called ErrorLog.log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s \n')
# this line tells the file what format to put the message in
fileHandler.setFormatter(formatter) # set up the file with the format
log.addHandler(fileHandler) # add that file to our log

# now we can start off our log with this message
log.info("Starting log and executing program")

# When Python encounters an unhandled exception its default behavior is to print
# the traceback to the screen and quit, we can add in our own behavior by creating
# a three argument function and assigning it to sys.excepthook
# https://docs.python.org/3/library/sys.html#sys.excepthook
def CustomExceptionHandler(exceptionType, value, traceback):
    # add a CRITICAL level log message to our log file saying what went wrong
    log.critical('Encountered an uncaught exception of type: ' + str(exceptionType) + ' \n' 
                 + str(value) + '\n'
                 )
    log.critical(tb.format_tb(traceback)) # use traceback module to format stack trace
    
    # after we are done logging we can call the default excepthook function
    sys.__excepthook__(exceptionType, value, traceback)

sys.excepthook = CustomExceptionHandler # assign our handler to be used
# note that this will NOT work in the IPython console because of how IPython 
# handles exceptions differently
# http://stackoverflow.com/questions/1261668/cannot-override-sys-excepthook
# and only works unreliably in Spyder, run in the command line

# ------------------------
# MAIN PART OF OUR PROGRAM
# ------------------------

# cause an error
x = 8 / 0 

