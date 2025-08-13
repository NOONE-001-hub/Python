class Employee:
    def __init__(self):
        print("Consructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Consructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Consructor of Manager")
    c = 3

# o = Employee()
# print(o.a) # Prints the a attribute
# print(o.b) # shows an error as there is no b attribute in employee class

# o = Programmer()
# print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)