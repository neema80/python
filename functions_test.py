def square(arg1, arg2):
    """if you hover your mouse over the function
    in other lines, this DocString will appear
    for this example check line 6 of this example"""
    return arg1 + arg2
value = square(10,50)
print(value)
# it is just a simple function
# we can assign a default value by changing the first line as below
def square1(arg1=10,arg2=50):
    """This adds to numbers together, 
    default values are 10 and 50"""
    return arg1 + arg2
print(square1())

# when we use print statement inside a function it wont be assigned to any
# variable outside the function but instead of we use return statement
# we can assign the returned value from function to the variable