class Employee:
    def show(self):
        print("emp class instance method")

    @staticmethod
    def display():
        print("emp class static method")

Employee.display()
e1=Employee()
e1.show()
e1.display()
Employee.show()
