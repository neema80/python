# if you put lamda inside the function the return statement is not necessary
# syntax
# lambda arg1, arg2, ...., arg n: an expression using the arguments
a = lambda x, y: x * y
print(a,"type is: ", type(a))
print(a(10,20))

# we can combine lambda function with list comprehension inside a nested for loop

# an exercise to pass the range of 10 and range of 5 multiplied to gether and
# export the result in a list concatenated with the list argument
# the old fasion way we do as follow
def myfunc(mylist):
    list_xy = []
    for i in range(10):
        for j in range(5):
            result = i * j
            list_xy.append(result)
    return list_xy + mylist
print(myfunc([100,101,102]))

# now do this in one line of code with list comprehension and lambda function
generator = lambda mylist: [x * y for x in range(10) for y in range(5)] + mylist
print(generator([100,101,102])) # same result as above

##### some common functions that are often used in conjunction with lambda function are
# map and filter
# simple example
def myfunc1(arg):
    return arg * 10
r1 = range(10)
print(list(map(myfunc1, r1)))
# now lets do the same using the lambda function
print(list(map(lambda argument: argument * 10, r1)))

# filter is similar to map with the difference of only returns where the lambda returns true
print(list(filter(lambda argument: argument > 5, r1)))