#
# print("total = ", eval(input("enter some text: ")))
# the calculator app versio 1.0

while True:
    print(""" WELCOME TO CALCULATOR APP:
    To do the add enter 'add' 
    for multiplication enter 'multiply'
    for division enter 'division'
    for floor division and remainder enter 'floor'
    or 'quit' to end this app""")
    choose = input("Please choose your action from the above:")
    if choose == 'quit':
        break
    elif choose == 'add':
        print("add entered")
    else:
        print("Command not found!")