# a great module to work with iterator
from itertools import *

# chain()
list1 = [1,2,3,4,"a","b","c"]
list2 = [100,200,300,"X","Y","Z"]
print(list(chain(list1,list2))) # chain function makes an iterable of the arguments that we provide to it

# count()
# it iterates until we break the sequnce just like while True loop we have to be wise
for i in count(10,2.5):
    if i <= 50:
        print(i)
    else:
        break

# cycle()
# just similar to count() we have to be careful to break the cycle
# otherwise it would repeats infinately
count = 0
for i in cycle(range(1,100,6)):
    if count <= 10:
        print(count , i)
        count += 1
    else:
        break

# filterfalse()
# it is exactly opposite of filter() function and returns element where the iterator returns False

# islice()
# is similar to slicing but in a different manner
list1 = list(range(10))
list1 = list1[2:9:2] # starting from 2 # end to 8 with step of 2
# just normal slicing
print(list1)
print(list(islice(range(10),2,9,2)))