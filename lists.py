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
num1.insert(2, 300)

print(num1)
num1.remove(300)
print(num1)
print(num1.pop())
print(num1)
