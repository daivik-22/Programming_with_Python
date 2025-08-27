# Expt 2.1.8 Applications of Dictionary
# Application: Student Management System using Dictionary
# Each student has a roll number as key and details as value (name, marks in 3 subjects)
students = {
 101: {"name": "Daivik", "marks": {"Math": 88, "Science": 92, "English": 85}},
 102: {"name": "Vikram", "marks": {"Math": 78, "Science": 81, "English": 79}},
 103: {"name": "Aleshya", "marks": {"Math": 90, "Science": 87, "English": 91}},
 104: {"name": "Meghana", "marks": {"Math": 85, "Science": 89, "English": 84}},
 105: {"name": "Ali", "marks": {"Math": 92, "Science": 95, "English": 90}}
}

# Print all student details
print("Student Records:")
for roll_no, info in students.items():
 print(f"Roll No: {roll_no}, Name: {info['name']}, Marks: {info['marks']}")

# Find student with highest total marks
topper = max(students.items(), key=lambda x: sum(x[1]["marks"].values()))
print(f"\nTopper: Roll No: {topper[0]}, Name: {topper[1]['name']}, Total Marks:
{sum(topper[1]['marks'].values())}")

# Calculate average marks in each subject
subjects = ["Math", "Science", "English"]
print("\nAverage marks in each subject:")
for subject in subjects:
 avg = sum(info["marks"][subject] for info in students.values()) / len(students)
 print(f"{subject}: {avg:.2f}")

# List students who scored above 90 in any subject
print("\nStudents who scored above 90 in any subject:")
for roll_no, info in students.items():
 if any(mark > 90 for mark in info["marks"].values()):
 print(f"Roll No: {roll_no}, Name: {info['name']}, Marks: {info['marks']}") 
