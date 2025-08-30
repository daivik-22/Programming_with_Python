import re
Daivik = "The price is [100 dollars] and the discount is [20 percent] only."
print(re.findall(r"\[.*\]", Daivik))   # Greedy
print(re.findall(r"\[.*?\]", Daivik)) # Lazy
