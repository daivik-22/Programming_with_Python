# Creating a List
daivik = [1, 2, 3, 4, 5]
print("Initial list:", daivik)
# Accessing Elements
print("First element:", daivik[0])
print("Last element:", daivik[-1])
# Modifying Elements
daivik[2] = 10
print("After modifying index 2:", daivik)
# Adding Elements
daivik.append(6)
daivik.insert(1, 99)
print("After append and insert:", daivik)
# Removing Elements
daivik.remove(99)
popped = daivik.pop()
print("After remove and pop:", daivik)
print("Popped value:", popped)
# Slicing
sub_list1 = daivik[1:4]
sub_list2 = daivik[-1:3] 
# This slice will return an empty list because step is default (forward)
print("Sliced list (index 1 to 3):", sub_list1)
print("Sliced list (last element to index 3):", sub_list2)
# Iterating through a List
print("Iterating through list:")
for item in daivik:
 print(item)
# Checking Membership
if 10 in daivik:
 print("10 is in the list")
else:
 print("10 is not in the list")
# Length of List
print("Length of list:", len(daivik))
# Concatenating Lists
list2 = [7, 8]
combined = daivik + list2
print("After concatenation:", combined) 
