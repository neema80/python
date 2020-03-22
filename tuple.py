# tuples instead of the list are immutable and are formatted in the () and lists are formatted inside []
tupl1 = 10,20,30,50,40,80
print(tupl1)
print(type(tupl1))
mylist = [60,70,100,90]
tupl2 = tuple(mylist)
tupl3 = tupl1 + tupl2
print(tupl3)
tupl4 = tupl3 + tupl3
print(tupl4.count(20)) #counts how many times number 20 is repeated in the tuple4
print(tupl3.index(40)) #gives us the position of the number 40 in the tuple
print(sum(tupl4))
print(max(tupl3))
print(min(tupl3))
print(sorted(tupl3)) # it sorts the tuple but also converts it to list
tupl3 = tuple(sorted(tupl3)) # we use the command tuple to change the format back to tuple again
print(tupl3)

# bear in mind when creating a tuple with just one element you have to put comma at the end
# otherwise system will read it as another type
# ie
tup1 = (1)
print(type(tup1),tup1)

tup1 = (1,)
print(type(tup1),tup1)
# tuple unpacking and even changing the final format to list
tup1 = ((10, 20), ("a", "b"),(100, 200))
print(tup1)
unpacked = []
for i, j in tup1 :
    print(i,j)
    unpacked.append(list((i,j)))
print(type(unpacked), unpacked)
print(list(tup1))