"""
 * Project: Comparing numbers.
 * Objective: Compare the values and show which is bigger.
 * Author: José Valdeir
 * Date: 08/01/2021
"""
num1 = int(input('Type a number: '))
num2 = int(input('Type a second number: '))

if num1 > num2:
    print(f'The number {num1} is bigger than {num2}.')
elif num1 == num2:
    print(f'The number {num1} and {num2} are the same!')
else:
    print(f'The number {num2} is bigger than {num1}')
