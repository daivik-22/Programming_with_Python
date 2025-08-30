import re
Daivik = "The years 1999, 2023, and 2050 were mentioned."
numbers = re.findall(r"\b\d{4}\b", Daivik)
print(numbers)
