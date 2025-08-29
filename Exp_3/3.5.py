# Expt 3.5 – Inheritance
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

m = Manager("Vikram", 50000, "IT")
print(m.name, m.department)
