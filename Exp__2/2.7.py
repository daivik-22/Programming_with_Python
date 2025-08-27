# Expt 2.1.7 Dictionary Operations
# Creating a dictionary
student_daivik = {
 "name": "Daivik",
 "age": 20,
 "course": "Python"
}
print("Original Dictionary:", student_daivik)

# Accessing values
print("Name:", student_daivik["name"])
print("Age:", student_daivik.get("age"))

# Adding a new key-value pair
student_daivik["grade"] = "A"
print("After adding grade:", student_daivik)

# Updating a value
student_daivik["age"] = 21
print("After updating age:", student_daivik)

# Removing a key-value pair
del student_daivik["course"]
print("After removing course:", student_daivik)

# Iterating through dictionary
print("All key-value pairs:")
for key, value in student_daivik.items():
 print(key, ":", value)
