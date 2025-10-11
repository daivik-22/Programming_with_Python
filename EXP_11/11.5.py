import re 
hero_regex = re.compile(r'Batman|Tina Fey')
mo = hero_regex.search('Batman and Tina Fey.')
print(mo.group())
