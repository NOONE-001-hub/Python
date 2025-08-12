class Employee:
    language = "Python" # This is class attribute
    salary = 1200000

kanna = Employee()
kanna.language = "JavaScript" # This is an instance attribute
print(kanna.language, kanna.salary) 
 