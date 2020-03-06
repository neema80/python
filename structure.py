####################### 1 ##########################
num = [10, 20, 30, 40]
add_up = eval( "{} + {} + {}".format( max( num ), min( num ), sum( num ) ) )
print(add_up)

###################### 2 ##########################
pay_slip1 = ["A", "data scientist", "B", "Omar", "c", 55000]
pay_slip2 = ["A", "python developer", "B", "Gemma", "c", 34000]
pay_slip1 = pay_slip1[1:6:2] # or pay_slip1 = pay_slip1[1::2]
pay_slip2 = pay_slip2[1:6:2]
print( pay_slip1, pay_slip2 )
Omar = """###The !!!annual### salary!!!, for {} {}### is!!! ${} + ${} Bonus""".format(*pay_slip1, 7000 ).replace( "###", "" ).replace( "!!!", "" )
Gemma = """###The !!!annual### salary!!!, for {} {}### is!!! ${} + ${} Bonus""".format(*pay_slip2, 7000 ).replace( "###", "" ).replace( "!!!", "" )
print( Omar )
print( Gemma )

###################### 3 ##########################
mylist = [100+100 is not 200,
 "c" in "cats",
 100+100 is 200,
 5 <= 500 > 100,
 10 is  eval("10"),
 40 != 40,
 10 == 10 and 12 is not 10]
print(mylist)

##################################################
pals = ["kitten", "puppy", "owl", "duck"]
print("""there is a cute {1} and a tiny {0} playing with a {3} next to an {2}""".format(*pals).upper().split()[4::4])
