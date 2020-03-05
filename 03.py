__author__ = "Nima"

a = 10
b = 25
c = 100
d = ("cat", "dog", "bird")
if a == 100:
    if b < 45:
        print("This is True!")
    else:
        print("a is {} so This is false!".format(a))
else:
    print("a is {} so This is false!".format(a))
if a == 10:  # nested logical statement
    # as the python is interpreter is it important if the condition is not true then it will ignore the rest
    # automatically
    print("a is true!")
    if b < 45:
        print("b is True!")
        if c == 100:
            print("c is true!")
            if "zebra" in d:
                print("d is true!")
            else:
                print("d is false!")
        else:
            print("c is false!")
    else:
        print("b is false!")
else:
    print("a is false!")

# num = eval(input("Enter a number: ")) # by default the format is tring if we want to calculate it we have to change
# the format using the eval function print("number is {}".format(num), " type is: ", type(num))
#
# now we use this input for searching in the touple
# if num >= 3 :
#    print("Keep Looking!")
# elif d[num] == "cat" :
#    print("Found a {}".format(d[num]))
# elif d[num] == "dog" :
#    print("Found a {}".format(d[num]))
# else :
#    print("Found a {}".format(d[num]))

list = [list(range(11)), list(range(11, 21)), list(range(21, 31))]
print(list)
v = eval(input("Enter a number: "))
if v in list[0]:
    print(v, " is in list one")
elif v in list[1]:
    print(v, "is in list two")
elif v in list[2]:
    print(v, "is in list three")
else:
    print(v, "is not in the list!")
