# Expt 2.1.2 Applications of List
# Application: Storing and processing student marks using a list
# List of student marks
daivik = [85, 90, 78, 92, 88]
print("Student Marks:", daivik)
# Adding a new mark
daivik.append(95)
print("After adding a new mark:", daivik)
# Removing a mark
daivik.remove(78)
print("After removing a mark:", daivik)
# Calculating average
average = sum(daivik) / len(daivik)
print("Average Marks:", average)
# Sorting marks
daivik.sort()
print("Sorted Marks:", daivik)
# Finding the highest and lowest marks
highest = max(daivik)
lowest = min(daivik)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest) 
