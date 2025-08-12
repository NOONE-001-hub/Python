class Employee:
    language = "Python" # This is class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name 
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


kanna = Employee("Kanna", 1300000, "Javascript", )
# kanna.name = "Kanna"
print(kanna.name, kanna.salary, kanna.language)
