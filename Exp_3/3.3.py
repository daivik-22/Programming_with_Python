# Expt 3.3 – Student Class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Daivik", 90)
s1.display()
