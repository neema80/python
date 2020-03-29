# this is a method where a function returns a function as a result
# instead of the processed argument
# it acts like a black box

def create_printer():
    def printer():
        print('Hello functional!')
    return printer

my_printer = create_printer()
my_printer()

# instead of whole following lines we could do as it suggested after line #21
# def double(x):
#     return x * 2
# def triple(x):
#     return x * 3
# def quadruple(x):
#     return x * 4

# (a) is the multiplier argument and (x) is going to be passed when it is been called
def create_multiplier(a):
    def multiplier(x):
        return x * a
    return multiplier

double = create_multiplier(2) # (a) = 2
triple = create_multiplier(3) # (a) = 3
quadruple = create_multiplier(4) # (a) = 4

print(double(eval(input("Enter radios of the circle: ")))) # (x) = from input()
print(triple(6)) # (x) = 6
print(quadruple(7)) # (x) = 7
# as it proves the code reusability and readability has improved very much