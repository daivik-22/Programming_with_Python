# Expt 2.1.6 Applications of Tuples
# Application: Storing and processing student records using tuples
# Each student record is a tuple: (roll_no, name, marks)
students = [
 (101, "Daivik", 88),
 (102, "Vikram", 92),
 (103, "Aleshya", 79),
 (104, "Meghana", 85),
 (105, "Ali", 90)
]

# Print all student records
print("Student Records:")
for student in students:
 print(f"Roll No: {student[0]}, Name: {student[1]}, Marks: {student[2]}")

# Find the student with the highest marks
topper = max(students, key=lambda x: x[2])
print(f"\nTopper: Roll No: {topper[0]}, Name: {topper[1]}, Marks: {topper[2]}")

# Calculate average marks
average = sum(student[2] for student in students) / len(students)
print(f"Average Marks: {average}")

# List of students who scored above 85
print("\nStudents who scored above 85:")
for student in students:
 if student[2] > 85:
 print(f"Roll No: {student[0]}, Name: {student[1]}, Marks: {student[2]}") 
