
# This order matters!
# Obs: can use inner exceptions, catched by outsiders
# SystemExit untreated closes the program
try:
    pass # code tryin to execute
    raise  Exception("My message") # +- for error
    assert (1 > 0), "My message" # another type of raising
except ArithmeticError: # first must catch specific errors
    pass
except EnvironmentError as mYError: # can catch with name too
    pass
    x = mYError.args # arguments
except (TypeError, EOFError): # catch other general errors, can  group them
    pass
else: # executes if no exception happens
    pass
finally: # exeecutes in any case  (exception / no exception)
    pass


############
# MODULES
###########
# import module1 [as x], module 2 [as y] etc
# from module1 import Class/Func
# from module1 import * (import everything)

# SYS
import sys
args = sys.argv # first is the filepath

# OS
import os
# os.path = important functions for path (eg. isdir, isfile etc)
# os.listdir, os.mkdir
for (root,directories,files) in os.walk("."):
    pass # go down in recursion, starting with '.'

# IO
input("enter message") # read kb
print("message", 10, sep="-") # print kb. iterators, using separator

# files - usually use in a try
fobject = open("path", "r/w/rb/wb/a/rt")
for line in fobject:
    pass # read line by line
byteswritten = fobject.write(1024) # write buffered
bytesread = fobject.read("DDD", 1024) # read buffered
fobject.close()

