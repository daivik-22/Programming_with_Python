Code:
# Expt 2.1.5 Tuple Operations
# Creating a Tuple
daivik = (10, 20, 30, 40, 50)
print("Original Tuple:", daivik)

# Accessing elements in a Tuple
print("First element:", daivik[0])
print("Last element:", daivik[-1])

# Slicing a Tuple
print("Sliced Tuple (index 1 to 4):", daivik[1:4])

# Length of tuple
print("Length of Tuple:", len(daivik))

# Concatenating tuples
daivik1 = (60, 70, 80)
combined_daivik = daivik + daivik1
print("Concatenated Tuple:", combined_daivik)

# Repeating tuples
print("Repeated Tuple:", daivik * 2)

# Checking membership
print("Is 30 in the tuple?", 30 in daivik)

# Iterating through a tuple
print("Element in the tuple: ")
for element in daivik:
 print(element, end=' ') 
