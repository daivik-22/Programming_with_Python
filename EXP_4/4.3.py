import re
Daivik = "Welcome to Python programming"
match = re.search(r"Python", Daivik)
print(match.span() if match else "No match")
