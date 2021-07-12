"""
 * Project: List with pair and odd.
 * Objective: List with pair and list with odd numbers, in same list.
 * Author: José Valdeir
 * Date: 18/01/2021
"""
numbers = [[], []]
while True:
    num = int(input('Enter a number: '))
    if num % 2 == 0:
        numbers[0].append(num)
    else:
        numbers[1].append(num)

    while True:
        continua = input('Do you want to continue? [Y][N]')
        if continua not in 'YyNn':
            print('Wrong choice. Try again.')
        else:
            if continua in 'NnYy':
                break
    if continua in 'Nn':
        break
numbers[0].sort()
numbers[1].sort()
print(f'The pair values are: {numbers[0]}')
print(f'The odd values are: {numbers[1]}')
