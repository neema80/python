# if you put lamda inside the function the return statement is not necessary
# syntax
# lambda arg1, arg2, ...., arg n: an expression using the arguments
a = lambda x, y: x * y
print(a,"type is: ", type(a))
print(a(10,20))

# we can combine lambda function with list comprehension inside a nested for loop
