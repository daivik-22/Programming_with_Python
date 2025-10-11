import re
phone_regex = re.compile(r'\(\d{3}\)\s\d{3}-\d{4}')
mo = phone_regex.search("My number is (415) 555-4242.")
print("Phone number found:", mo.group())
