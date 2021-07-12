"""
 * Project: The bigger number.
 * Objective: Show which is the sort from three numbers.
 * Author: José Valdeir
 * Date: 08/01/2021
"""
n1 = int(input('Type a number: '))
n2 = int(input('Type other number: '))
n3 = int(input('Type the third number: '))

if n1 > n2:
    if n1 > n3:
        print(f'The number {n1} is the bigger number.')
else:
    if n2 > n3:
        print(f'The number {n2} is the bigger.')
    else:
        print(f'The number {n3} is the bigger.')
