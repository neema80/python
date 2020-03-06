d1 = {}
print(type(d1))
d1["A"] = 1
d1["B"] = 2
print(d1)
toys = {"robots": "$25.90", "cars": "$45.30"}
print(toys)
# we cannot use d1 + toys so we have to use update method
d1.update(toys)
print(d1)
d1["A"] = 120 # we just updated the value of the key "A"
print(d1)
# to remove a key from dictionary we use the pop method
d1.pop("A")
print(d1)
d1.values() # shows us the values of the dictionary but for indexing have to convert it to list or tuple
mylist = list(d1.values())
print(mylist)
mytupl = tuple(d1.values())
print(mytupl)
# for indexing
print(mylist[1:3])
# items function will shows us the contents of the dictionary as a nested touple inside a list
print(d1.items())
newlist = list(d1.items())
print(newlist)
print(type(newlist[0][0]))
menu = [("soup", 2.20),("chips", 1.4)]
print(menu)
d2 = dict(menu) # convert the nested touple into a dictionary
print(d2)