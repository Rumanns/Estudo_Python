"""
 * Project: Analyser of numbers on tupla.
 * Objective: Analyse numbers on tupla.
 * Author: José Valdeir
 * Date: 10/01/2021
"""
num = (int(input('Enter a number: ')),
    int(input('Another number: ')),
    int(input('One more: ')),
    int(input('The last: ')))
print(f'The number entered are: {num}')

print(f'The number 9 appears {num.count(9)} times')
if 3 in num:
    print(f'The number 3 was entered in position {num.index(3)+1}')
else:
    print('The value 3 was not entered!')
print(f'The pair numbers are: ', end='')
for par in num:
    if par % 2 == 0:
        print(f'{par}, ', end='')
