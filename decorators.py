# a sample decorator function
def decor(func):
    def wrap():
        print("===================")
        func()
        print("===================")
    return wrap
def print_text():
    print("Hello World!")
decorated = decor(print_text)
decorated()

## This is another method to call the decorator used upon the function defined below
@decor
def print_text1():
    print("Hello World using @decor method!")
print_text1()
