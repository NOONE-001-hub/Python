class Employee:
    language = "py" # This is class attribute
    salary = 1200000

kanna = Employee()
kanna.name = "kanna" # This is an instance attribute
print(kanna.name, kanna.language, kanna.salary) 

# here name is the instance attribute whereas salary and language are class attribute as they directly belong to class 