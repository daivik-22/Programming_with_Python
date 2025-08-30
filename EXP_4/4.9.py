import re
Daivik = "Abc@1234"
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
print("Strong password" if re.match(pattern, Daivik) else "Weak password")
