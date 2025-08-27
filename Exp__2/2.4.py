# Expt 2.1.4 Application of Set
# Application of set
# Finding students who take at least one subject and those who take only one subject
math_students = {"Daivik", "Vikram", "Aleshya"}
science_students = {"Ali", "Meghana", "Ram"}
social_students = {"Vikram", "Aleshya", "Riya"}

# Union: Students who take at least one subject
all_students = math_students | science_students | social_students
print("Students in at least one subject (Union):", all_students)

# Difference: Students who take only Math
only_math = math_students - science_students - social_students
print("Students who take only Math:", only_math)

# Difference: Students who take only Science
only_science = science_students - math_students - social_students
print("Students who take only Science:", only_science)

# Difference: Students who take only Social Studies
only_social = social_students - math_students - science_students
print("Students who take only Social Studies:", only_social) 
