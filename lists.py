first: range = range(0,21)
print(first)
print(list(range(0, 21)))

print(list(range(0, 21, 2)))

print(type(first))

num: list = [10, 20, 30, 40]

print(type(num))
num.append(100)
num.append(110)
print(num)

num.clear()
print(num)

#num.append([10, 50, 20, 40, 30])
#num = num[0]
num1: list = [10, 50, 20, 40, 30]
print(num1)
num1.insert(2, 300) # append to the list in the specific index

print(num1)
num1.remove(300) # removing an item from a list
print(num1)
print(num1.pop())
print(num1)
print(sorted(num1)) # sorting the list

# list comprehension ######
# normally is defined like this
count = []
for i in range(0,11):
    if i>3 and i % 2 == 0:
        item = i ** 3
        count.append(item)
print(count)
# whith list comprehension this will be done in one line
print([i**3 for i in range(0,11) if i>3 and i % 2 == 0])
print([i for i in 'universe']) # works for text

############# control flow in list comprehension
numbers = [20, 10, 30, 40, 50 , 70, 60, 90, 80]
print([i + 1 if i > 50 else i + 5 for i in numbers])
# contains a comprehension with if statement included
# the else statement means elif from left to right if there are many else in one line
print(["Run" if i % 2 == 0 else "Jump" if i == 3 else "Walk" for i in range(0,11)])