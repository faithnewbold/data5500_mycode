class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self): 
        return "Employee Name: " + (self.name) + ", their current salary is " + str(self.salary) 

    def increase(self, percentage):
        self.salary *= (1 + percentage / 100) #this allows you to increase it by a given percentage.

emp1 = Employee("John", 5000)

emp1.increase(10)

print(f"The new salary for {emp1.name} is: {emp1.salary}")