import re
Daivik = "Loving the #Python and #Regex journey! #CodingLife"
hashtags = re.findall(r"#\w+", Daivik)
print(hashtags)
