def add(x, y):
    return x + y
def subtract(x, y):
    return x - y

def combine_2_and_3(func):
    return func(2, 3)
print(combine_2_and_3(add)) # the inside function can be anything like min() or max()
print(combine_2_and_3(subtract))
print(combine_2_and_3(max))

def combine_names(func):
    return func('Neema', 'Bahram')
def append_with_space(first, last):
    return f'{first} {last}'

def get_government_form_notation(first, last):
    return f'{last.upper()}, {first.upper()}'

print(combine_names(append_with_space))
print(combine_names(get_government_form_notation))