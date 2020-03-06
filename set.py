# set contains only unique elements and will remove duplicates
s1 = {2,2,2,2, 10,10,10 , 20, 20,30,40,100}
print(type(s1)," ",s1)
s2 = [10,10,20,30,1,1,1,2,2,2,3,4,5]
s2 = set(s2) # converts the s2 list to set
print(s2)
print(s1.union(s2)) # gathers all the elemets between the two sets
print(s1.intersection(s2)) # shows only shared items between the two
print(s1.difference(s2)) # shows only the items that are in the s1 set but not in s2
print(s2.difference(s1)) # acts opposite of the line above
s4 = {200, True, "cat"}
s1.update(s4) #merges the sets into s1
print(s1)
s1.add(500) # just adds an item into the set
print(s1)
s3 = {200, True, 2}
print(s1.issuperset(s3)) # all of the s3 is in s1
print(s3.issubset(s1)) # does s3 sub set of s1?