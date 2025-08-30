import re
Daivik = "Contact us at support@example.com or sales@myshop.org"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", Daivik)
print(emails)
