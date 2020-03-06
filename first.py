var1: str = "Nima"
var2: str = "Parichehr"
robot: str = "technologically"
words: str = "I saw a cat jump over the moon and into the clouds"
#print(var1.upper() + " is in love with " + var2)
#print("days left are {num: .3f}".format(num=100/3))
#print("{} is in love with {}".format(var1, var2).lower())
#print(robot[0:6])
#print()
#print(robot[1::2])
print(words," {}".format(words.split()[3:12:2] ))
print(len(words),len(words.split()))
s1: slice = slice(3,12,2)
print( "words. split is ", words.split()[s1] )
print( '"cat" in words.split is ', "cat" in words.split() )
print( '"cat" not in words.split is ', "cat" not in words.split() )
newwords: str = words.split()
verynewwords: str = " ".join(newwords).upper() # or can put as many space like in between the items
print(newwords, verynewwords)
pay: str = "I receive a total of $5000"
print(pay)
print(pay.split("$"), "first section ", pay.split("$")[0] , "second part ", pay.split("$")[1])

