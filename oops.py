class student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def getdata(self):
        self.name = input("enter your name:")
        self.mark = input("enter your marks:")

    def putdata(self):
        print(self.name, "\n", self.mark)


obj = student(" "," ")
obj.getdata()
obj.putdata()
