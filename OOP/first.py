# class is a datatype consist of its own variables attributes and functions
# functions ---> methods
# class is blueprint for creating an object
# object == instance of a clas
class myrouter(object):
    """This is a class that describes characteristics of a router"""
    # then we create __init__ method. this instantiate the class whenever it is called and defines 
    # some variables as well
    # self should always come first in defining each methos
    # and is a self refrence to the method
    # self always point to the current instance of the class
    def __init__(self, routername, model, serialno, ios):
        # now define object attributes
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios
    
    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("With the serial number of: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)

router1 = myrouter("R1", "2600", "123456", "12.4")
# to confirm that the object router1 is created
print(router1)
# to access atributes we can easily do this
print(router1.routername)
print(router1.model)
print(router1.serialno)
print(router1.ios)

# now to access the method of the class we can do this
router1.print_router("20200326")

router2 = myrouter("R2", "7200", "654321", "12.2")
router2.print_router("20200326")

# to change the attribute we simlpy can do
router2.ios = "12.3"
print(router2.ios)

# getattr and setattr are python default methods to manipulate attributes
print(getattr(router2, "ios"))
setattr(router2, "ios", "12.2")
print(getattr(router2, "ios"))

# to check if that attribute exists
print("Does router2 have attribute for ios?", hasattr(router2, "ios")) # should return True

# to delete specific attribute we use
delattr(router2, "ios")
print("Does router2 have attribute for ios? ", hasattr(router2, "ios")) # should return False

# to check if the object is instance of a class we can check by using
print("Is router2 instance of myrouter class? ", isinstance(router2,myrouter)) # should return True



