import re
Daivik = "Order 3 apples and 20 bananas."
result = re.sub(r"\d+", "#", Daivik)
print(result)
