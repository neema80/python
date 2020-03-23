# if we want to see how many functions are inside a module file after import we can
# use the dir command
import math
print(dir(math))
print(type(math.pi), math.pi) # this is a pi variable inside math module

# to make file uses less resources we can use from ... import ...


# to check what is the path variable of the system we can use as below
import sys
print(sys.path)
