# iterators iter() takes an iterable object as an argument and returns the iterator
mylist = [1,2,3,4,5,6,7,8]
for element in mylist:
    print(element)
# simple task
# now using iterator
my_iter = iter(mylist)
print(type(my_iter)) # we have created our first iterator
# now we should use another function called next to iterate thorough our iterator
print(next(my_iter)) # this command will prints out our elements inside iterator
# and gets the (StopIteration) exception when all the items exhausted
# the good use is we don't need to keep all the sequence in memory and only we can
# pick up the items we want and use less resource as a result besides it is considered an
# elegant way of coding

# generator is a routine that can control the behaviour of iteration loop 
# generator yields the values once at a time
# with this method we can iterate thorough an iterator and stop the action
# and again at certain point in time get back to the function and continue
# our generator therefore we used less resource again
def mygen(x,y):
    for i in range(x):
        print("i is %d", i)
        print("y is %d", y)
        print("i * y = {}".format(i*y))
        yield i * y # suspends the execution and returns the value back to the caller
    # also saves the state of the execution
my_object = mygen(10, 5)
print(type(my_object))
next(my_object) # as we have the print statement inside the function no need to use print
                # statement in this line of code
next(my_object)
next(my_object)
next(my_object) # (StopIteration) is an exception rise when we reach end of generator

#### generator expressions #####

genex = (x for x in range(5))
# I used the try except to show error message when the list has exhausted
try:
    while True:
        print(next(genex))
except:
    print("The list has exhausted")



 