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

########## *args #############
# used when we are not sure how many arguments our function will have
def tota(*args, z = 10):
    """This adds as many arguments together
    plus adds a default value of 10 assigned to z argument by default"""
    s = 0
    for i in args:
        s += i
    print(args)
    return s + z
print(tota(20,30,40))

######## **kwargs ###################
# this is returning a dictionary as an output
def Inventory(**kwargs):
    Players = {}
    for i in kwargs:
        Players.update({i: kwargs})
    return Players
print(Inventory(a="Nima",b="Ali",c="Reza"))
### another sample
def Flower_test(**kwargs):
    print(kwargs)
    if "Flower" in kwargs:
        print("we have {} flower for you!".format(kwargs["Flower"]))
    else:
        print("We don't have any flower for you")
Flower_test(color = 0, Flower = "Tulip")    