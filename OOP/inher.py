class myrouter(object):
    """This is a class that describes characteristics of a router"""
    def __init__(self, routername, model, serialno, ios):
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

# now we make a child class to inherit from the parent "myrouter"
# the child class can skip the __init__ method as it will inherit from its parent already
class mynewrouter(myrouter):
    # if requires to change attributes then totally new __init__ method should be written
    def __init__(self, routername, model, serialno, ios, portsno):
        myrouter.__init__(self, routername, model, serialno, ios)
        self.portsno = portsno
    def print_new_router(self, string):
        print(string + self.portsno)
router1 = mynewrouter("R1", "2600", "123456", "12.4", "10")
router1.print_new_router("how many ports does Router1 have? ")
router1.print_router("20200326") # this method is called from parent

# a child can inherit from multiple parents
# can be defined as below
# class child(parent1, parent2, parent3):

# to avoid circular refrence we can use following methods to check if the class is sub class of another one
print("does mynewrouter a subclass of myrouter? ", issubclass(mynewrouter, myrouter))



