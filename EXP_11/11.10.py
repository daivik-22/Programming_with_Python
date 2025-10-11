import re 
bat_regex = re.compile(r'Bat(wo)?man')
print(bat_regex.search('The Adventures of Batman').group())
print(bat_regex.search('The Adventures of Batwoman').group())
