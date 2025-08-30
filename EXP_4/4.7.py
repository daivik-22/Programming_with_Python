import re
Daivik = "15-08-2025"
match = re.match(r"(\d{2})-(\d{2})-(\d{4})", Daivik)
if match:
    day, month, year = match.groups()
    print(day, month, year)
