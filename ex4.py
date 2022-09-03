class test:
    m=25  #static variables
    def assign(self,a,b):
        print("a value is:",a)
        print("b value is:",b)
        self.c = a+b #instance variable
        print("sum is:",self.c)
        print("m value is :",test.m)
    def show(self):
        print("c value is:",self.c)
    @staticmethod
    def display():
        print("m value is:",test.m)

t=test() #refernce variable
p = int(input("enter any number:",))
q = int(input("enter any number:",))
t.assign(p,q) #parameter variable
t.show()
test.display()
