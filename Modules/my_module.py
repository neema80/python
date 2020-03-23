my_var = 10
def my_func():
    print("This statement is printed when called the function my_func")

print("This will be executed wherever the file is called")
# as the file will be used outside of this file
# if we want lines of code to be executed only inside the file
# we require an if block statement to take care of this
if __name__ == "__main__":
    print("This will be executed only inside this code")