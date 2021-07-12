"""
 * Project: Numeric base conversion.
 * Objective: Convert a number of decimal base for other.
 * Author: José Valdeir
 * Date: 08/01/2021
"""
num = (input('Enter a decimal base number: '))
base = int(input('Chose a base to convert:\n [1] Binary\n [2]Octal\n [3]Hexadecimal\nYour chose: '))
print({len(num)})

if base == 1:
    print(f'The number {num} in binary base is: {bin(num)[2:]}')
elif base == 2:
    print(f'The number {num} in octal base is: {oct(num)[2:]}')
elif base == 3:
    print(f'The number {num} in hexadecimal base is: {hex(num)[2:]}')
else:
    print(f'Try again')
