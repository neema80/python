import math

def double(x):
    return x * 2
def minus_one(x):
    return x - 1
def squared(x):
    return x * x

# we don't put the () after the name of the functions
# in that case we mean the result of the function to be used
# however in the following list we are looking for the functions itself and 
# does not care about the result of the function so we emit the () after the name of the function
# this list can be changed the way we want it to be at anytime
function_list = [
    squared,
    double,
    minus_one,
    math.sqrt, # we can import whatever functions from any modules that we like and add them
    # into our list of functions
]

my_number = 3

for func in function_list:
    my_number = func(my_number)

print(my_number)