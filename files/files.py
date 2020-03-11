# testing writing to a file

text = input("Enter a file name here: ")
file = open(text,"a")

sample = """ 
some new lines added
This is a sample text going to 
be written on the file
""" 
file.write(sample)
file.close()