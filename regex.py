# this is for searching inside a text file based on a patter
# the built in module re will help us do that
str = "You can learn any programming language, whether it is Python2, Python3, Perl, Java, javascript or PHP."

import re
a = re.match("You", str)
print(a) # to confirm if there is math otherwise it would be None
print(a.group()) # to see contents of the matched items

### optional flags will help us to ignore some items for
# this example we will ignore the uppercase or lowercase
a = re.match("you", str, re.I) # re.I will ignore the case sensivity
print(a.group()) # still we get the correct response

# the match method only works if the string is at the beggining of the string
# for other places we should use .search method
b = re.search("programming", str)
print(b.group())

# the exact use of regex is sampled below
arp = "92.50.28.121   0     b4:a9:5a:ff:c8:45 VLAN#222     L"
# "r"" at the beginning of the code means raw string and ignore the scape sequence"
# othewise the re module will get confused with all the escape sequences
# (.+?) means as many characters as you can until you reach the white space defined afterwards of ?)
# (\d) means only a digit
#  +(.+?)\s{2,} means a whitespace after that count as many characters as you can till you see
# a whitespace of two characters happens at the end that \s{2,} will do the trick
# . itself means any character except the new line character
# + means 1 or more repetition of the expression before it
# * means 0 or more repetition of the expression before it
# ? means match as minimal as you can and ignore the whitespace
# \s means any whitespace which can be space tab or anything
# {2,} means the occurance of the proceding character should repeated at least 2 times
# {2} means the occurance of the proceding character should repeated at exact 2 times
# \w means sequence of any word character A-Z , a-z, 0-9, also underscore character 
c = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)
print(c.group())
print(c.group(1))
print(c.group(2))
print(c.group(3))
print(c.group(4))
d = re.search(r"(.+)\s{2,} +(\d) +(.+?)  +(\w)*", arp) # similar to above code with slight changes in the format
print(d.group()) # equals to print(d.group(0))
# to extract the data inside a tuple we use .groups method
print(c.groups())
print(d.groups())
# the .findall method is byfar the best method where returns the list instead of tuple for each match
e = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", arp) # this line extracts the ip address
# [0-9] means characters between 0 to 9
# {1,3} means repeated at least 1 and maximum to 3
# \. is an special escape sequence meaning the dot itself
# as the . itself has special meaning.
print(e)
# to make the reports for grouping to happen we should put them inside ()
f = re.findall(r"([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})", arp)
print(f)
# as we see below it searches for the whole text and to find the exact matches
# and return them inside a list
newarp = "92.50.28.121   0     b4:a9:5a:ff:c8:45 VLAN#222   92.50.28.122  L"
g = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", newarp)
print(g)
# the .sub method will substitue a character with the pattern we provide it
# in this example the VLAN will be substituted to number 510
h = re.sub(r"#\d{1,3}", "510", newarp)
print(h)