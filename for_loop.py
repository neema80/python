for i in range(0,20,2) :
    print(i)
cats = ["tiger", "lion", "jaguar", "leopard"]
for c in cats :
    print(c)
    # it prints out the elemts in the list
    # similar to cats[c]

nest1 = [[10, 20, 30],[3.5, 4.5, 5.5],["sword","hammer","shield"]]
for i in range(3) :
    res = nest1[0][i] + nest1[1][i]
    print(nest1[2][i].capitalize() + ": Power Level =", res)
    print(nest1[2][i].upper() , ": Power Level =", res)
    # if we use + in the print func it concatenates the strings together
    # while if we use , it puts a space between strings

# reformatting of the above list
weapons = []
for i in range(3) :
    weapons.append(nest1[2][i].capitalize() + ": Power Level = " + str(nest1[0][i] + nest1[1][i]))
print(weapons)
items = eval(input("Enter Weapons item: "))
if items >= 0 and items <= 2 :
    print(weapons[items])
else :
    print("Item not found!!")

for i in range(1, 8) :
    print("{} + {} = {}".format(i,i,(i+i)))
for i in range(1, 8) :
    print("%d * %f = %f" % (i , i , (i*i)))
    # %d means integer
    # %f means float

cakes = ["chocolate", "lemon", "carrot", "vanilla"]
d1 = {"k1": tuple(cakes), "k2" : [10,20,30,40]}
for i in d1 :
    # print(i)
    # prints out the key elemts
    # for printing the elemets and values we use nested for loop
    for j in range(0,len(cakes)) :
        print(i ,":", d1[i][j])