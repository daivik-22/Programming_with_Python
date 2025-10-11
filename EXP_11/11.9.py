import re
no_newline_regex = re.compile(r'.*')
print(no_newline_regex.search("Serve the public trust.\nProtect the innocent.").group())
