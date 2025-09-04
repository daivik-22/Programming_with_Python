import sys, os
os.getcwd()
os.chdir(r"D:\2025-2026\ODD\Python Programming\Notes\Codes")
os.getcwd()

file = open('spam.txt,'w')
file.write(('spam'*5+'\n')
file.close()
file.open('spam.txt')
text = file.read()
text
