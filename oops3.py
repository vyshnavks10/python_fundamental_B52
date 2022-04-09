class computer:
    def __init__(self, getspecs, displayspecs):
        self.getspecs = getspecs
        self.displayspecs = displayspecs


class Desktop(computer):
    def __init__(self, height, cpu, gpu, ram, colour, coolent):
        self.height = height
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.colour = colour
        self.coolent = coolent

    def getspecs(self):
        self.height = "20inch"
        self.cpu = "i7 8core"
        self.gpu = "nvidia 1660"
        self.ram = "8gb"
        self.colour = "white"
        self.coolent = "liquid"

    def displayspecs(self):
        print("height of desktop:", self.height)
        print("cpu of desktop:", self.cpu)
        print("gpu of desktop:", self.gpu)
        print("ram of desktop:", self.ram)
        print("colour of desktop:", self.colour)
        print("coolent of desktop:", self.coolent, "\n")

        print("Laptop specifications""\n")


class Laptop(computer):
    def __init__(self, weight, height, cpu, gpu, ram, colour, coolent):
        self.weight = weight
        self.height = height
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.colour = colour
        self.coolent = coolent

    def getspecs(self):
        self.weight = "2kg"
        self.height = "17inch"
        self.cpu = "i7 6core"
        self.gpu = "nvidia 1660"
        self.ram = "8gb"
        self.colour = "black"
        self.coolent = "fan"

    def displayspecs(self):
        print("weight of desktop:", self.weight)
        print("height of desktop:", self.height)
        print("cpu of desktop:", self.cpu)
        print("gpu of desktop:", self.gpu)
        print("ram of desktop:", self.ram)
        print("colour of desktop:", self.colour)
        print("coolent of desktop:", self.coolent)


obj = Desktop(" ", " ", ",", ",", ",", "")
obj.getspecs()
obj.displayspecs()
obj = Laptop(" ", " ", "", "", "", "", "")
obj.getspecs()
obj.displayspecs()