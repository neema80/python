# testing writing to a file

text = input("Enter a file name here: ")
file = open(text,"a") # access mode of "x" checks and if the file is not exist then will create it
# this "x" mode also might except us on the user access mode if the user doesn't have
# the right permission to access the folder we want to create the file

sample = """ 
some new lines added
This is a sample text going to 
be written on the file
""" 
file.write(sample)
file.close()

# if we use the read on the file the position of the curser will move to the end of the file
# so we can use .seek and .tell to check where is the curser and even to manually change the location of it
# .readline is another method where it reads the content of the file line by line
# everytime the method is called upon
# .readlines also is another method where it reads all the line and puts all of them inside a list

# if the file is wanted to be located exactly for the back slashes should use \\ instead of \

################### writing #################33
# .writelines(["Cisco\n", "Juniper\n", "HP\n"])
# this will put the list into lines and write it back to the file
# if we don't enter \n the lines will be concatanated all together

################# access modes
# "r+" , "w+" , "a+"
# if we use "w+" it opens the file for reading and writing and also if does not exist then will
# create it for us

###### with ..... as .....
# this method will take care of the closing the file automatically
with open("sample.txt","w") as f:
    f.write("This is a sample text\n")
