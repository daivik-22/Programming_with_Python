import re

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

test_passwords = ["Daivik123", "Strong@Pass1", "weakpass", "HelloWorld1!"]
for pwd in test_passwords:
    print(f"{pwd} ->", "Strong" if is_strong_password(pwd) else "Weak")
