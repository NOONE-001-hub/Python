class Employee:
    language = "Python" # This is class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


kanna = Employee()
# kanna.language = "JavaScript" # This is an instance attribute 
kanna.greet()
kanna.getInfo()
# Employee.getInfo(kanna)
