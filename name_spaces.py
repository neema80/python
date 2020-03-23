# built-in functions are for python and we are not needed
# to define them prior to using them
print(list(range(10)))
# NameError is the erros message raised when we see if we haven't defined them earlier
my_var = 10
print("This is a global variable: ", my_var)
# it is a global variable
# the variables are defined below a functions for example is considered a local variable
# and cannot be called outside of the function
def my_func():
    my_var = 20
    print("This is a local variable in namespace my_func: ", my_var)
my_func()
print("This is a global variable: ", my_var) # this my_var still looks inside global variables

# if we decide to import a global variable inside a local namespace like function we
# should mention global <var_name> to define it there
def my_func1():
    global my_var
    print("This is a global variable imported into my_func1: ", my_var)
    # having the empty return statement and nothing retursn None to the caller
    return
my_func1()
x = my_func1() # assignment from None error
# by using this method we can call an inside variable outside of the namespace
print(x)
