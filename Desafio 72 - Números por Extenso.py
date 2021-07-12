"""
 * Project: Number in full
 * Objective: Read a number and write it down.
 * Author: José Valdeir
 * Date: 10/01/2021
"""
numext = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
          'dezoito', 'dezenove', 'vinte')

while True:
    again = ' '
    while True:
        num = int(input('Enter a number between 0 and 20: '))
        if 0 <= num <= 20:
            break
        print('Invalid number. Try again.')

    print(f'The number entered was: {numext[num]}')
    while again not in 'SN':
        again = str(input('Do you like to enter another number? [S/N] ')).upper().strip()[0]
        if again == 'N':
            break
    if again == 'N':
        break
print('Program ended!')
