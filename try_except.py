# we use try and except method to change the error messages that system
# generates and make our own error messageg
for i in range(5):
    try:
        print(i/2)
    except ZeroDivisionError as e: # e is a variable for usage
        # however it is not mandatory but is good practice for better code maintaining
        print(e,"--> sorry! you cannot divide by number zero")
        print("sorry cannot do")

##### multiple except statement is allowed and
# also can use except statement alone to use as a catch all method for rest of the excepts
    except NameError:
        print("Error in Naming")
    except ValueError:
        print("Error in value")
    except:
        print("an error happened")
    # the else statement can be used similar to while and for loop
    # to use if no exception is raised during the code
    else:
        print("this is the else statement of the try block")
    # finally statement always come at the end of the block
    # and always gets processed either way
    finally: 
        print("I don't care I would be written any ways if there are errors or not")
else:
    print("the loop is now finished")