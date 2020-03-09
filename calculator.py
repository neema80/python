#! /usr/bin/python3
# print("total = ", eval(input("enter some text: ")))
# the calculator app versio 1.0

while True:
    print(""" WELCOME TO CALCULATOR APP:
    To do the add enter 'add'
    for minus enter 'minus' 
    for multiplication enter 'multiply'
    for division enter 'division'
    for floor division and remainder enter 'floor'
    for power enter 'exponentiation'
    or 'quit' to end this app""")
    choose = input("Please choose your action from the above: ")
    if choose == 'quit':
        break
    elif choose == 'add':
        val1 = float(input(print('enter first value: ')))
        val2 = float(input(print('second value: ')))
        result = val1 + val2
    elif choose == 'division':
        val1 = float(input(print("enter first value: ")))
        val2 = float(input(print("second value: ")))
        result = val1 / val2
    elif choose == 'minus':
        val1 = float(input(print("enter first value: ")))
        val2 = float(input(print("second value: ")))
        result = val1 - val2
    elif choose == 'floor':
        val1 = float(input(print("enter first value: ")))
        val2 = float(input(print("second value: ")))
        result = val1 // val2
    elif choose == 'exponentiation':
        val1 = float(input(print("enter first value: ")))
        val2 = float(input(print("second value: ")))
        result = val1 ** val2
    else:
        print("Command could not found!")
    print("total = ", result)