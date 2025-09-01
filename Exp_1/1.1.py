# Exp 1.1
import math
daivik_x = float(input('Enter the first number: '))
daivik_y = float(input('Enter the second number: '))

# Available operations
print("Operations: +, -, *, /, //, %, **")
daivik_opp = input('Enter the desired operation: ')

if daivik_opp == '+':
    daivik_total = daivik_x + daivik_y
    print(f'The Sum of {daivik_x} and {daivik_y} = {daivik_total}')

elif daivik_opp == '-':
    daivik_total = daivik_x - daivik_y
    print(f'{daivik_x} - {daivik_y} = {daivik_total}')

elif daivik_opp == '*':
    daivik_total = daivik_x * daivik_y
    print(f'{daivik_x} * {daivik_y} = {daivik_total}')

elif daivik_opp == '/':
    daivik_total = daivik_x / daivik_y
    print(f'{daivik_x} / {daivik_y} = {daivik_total}')

elif daivik_opp == '//':
    daivik_total = daivik_x // daivik_y
    print(f'{daivik_x} // {daivik_y} = {daivik_total}')

elif daivik_opp == '%':
    daivik_total = daivik_x % daivik_y
    print(f'{daivik_x} % {daivik_y} = {daivik_total}')

elif daivik_opp == '**':
    daivik_total = daivik_x ** daivik_y
    print(f'{daivik_x} ** {daivik_y} = {daivik_total}')

else:
    print('Error: Invalid operation')

# Extra calculations 1
daivik_red = (24 * 6**2) / (7 - 2)
print("Result 1:", daivik_red)

# Extra calculations 2
daivik_edf = 23 / (934 * (3 + 4**3))
print("Result 2:", daivik_edf)

# Extra calculations 3
x_daivik = math.sqrt(23) ** 3
print("Extra sqrt power:", x_daivik)
