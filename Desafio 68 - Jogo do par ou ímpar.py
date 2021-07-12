"""
 * Project: Pair or Odd.
 * Objective:
 * Author: José Valdeir
 * Date: 10/01/2021
"""
import random
v = 0
while True:
    escolha1 = ' '
    escolha2 = ' '
    while escolha1 not in 'PI':
        escolha1 = str(input('What do you want? Pair or Odd? [P/I] ')).upper().strip()
    pc = random.randint(0, 10)
    p1 = int(input('Choose a number in 1 and 10:  '))
    total = pc + p1
    if total % 2 == 0:
        if escolha1 == 'P':
            print(f'{pc} + {p1} = {total}, You win!  \o/')
            v += 1
        else:
            break
    if total % 2 == 1:
        if escolha1 == 'I':
            print(f'{pc} + {p1} = {total}, You win!  \o/ ')
            v += 1
        else:
            break
print(f'{pc} + {p1} = {total}, I win!!\n'
      f'You has {v} Victories!!!')
