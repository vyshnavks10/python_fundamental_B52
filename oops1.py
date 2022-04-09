

#  Using the concept of object oriented programming and inheritance, create
#  a super class named Computer, which has two sub classes named Desktop
#  and Laptop. Define two methods in the Computer class named getspecs
# and displayspecs, to get the specifications and display the specifications of
# the computer. You can use any specifications which you want. The Desktop
# class and the Laptop class should have one specification which is exclusive
# to them for example laptop can have weight as a special specification. Make
# sure that the sub classes have their own methods to get and display their
# special specification. Create an object of laptop/ desktop and make sure to
# call all the methods from the computer class as well as the methods from the own class
class computer:
    def __init__(self, getspecs, displayspecs):
        self.getspecs = getspecs
        self.displayspecs = displayspecs
    def getspecs(computer);

        def __init__(self, height, cpu, gpu, ram, colour, coolent):
            self.height = height
            self.cpu = cpu
            self.gpu = gpu
            self.ram = ram
            self.colour = colour
            self.coolent = coolent
            def diplayspecs (computer);
                self.height = "20inch"
                self.cpu = "i7 8core"
                self.gpu = "nvidia 1660"
                self.ram = "8gb"
                self.colour = "white"
                self.coolent = "liquid"


class Desktop(computer):
    def __init__(self,coolent):
        self.coolent = coolent

    def getdata(self):
        self.coolent = "liquid"

    def display(self):
        print("coolent of desktop:", self.coolent,"\n")

        print("Laptop specifications""\n")

class Laptop(computer):
    def __init__(self,weight):
        self.weight =weight

    def getdata1(self):
        self.weight = "2kg"


    def display1(self):
        print("weight of desktop:", self.weight)

# obj=computer("","")
# obj.getspecs()
# obj.displayspecs()
obj = Desktop(" ", )
obj.getdata()
obj.display()
obj = Laptop(" ", )
obj.getdata1()
obj.display1()
