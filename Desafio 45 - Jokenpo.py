"""
 * Project: Jokenpo.
 * Objective: Play Jokenpo.
 * Author: José Valdeir
 * Date: 09/01/2021
"""

import random
lista = [1,2,3]
jok = random.choice(lista)
num = int(input('[1] Rock[1]\n'
                '[2] Paper[2]\n'
                '[3] Scissor!?♫♪\n'))
if num > 0 and num < 4:
    if jok == 1 and num == 2:
        print('You Win! Congratulations!')
    elif jok == 2 and num == 3:
        print('Omg! You Win!')
    elif jok == 3 and num == 1:
        print('Oh, ok... You Win.')
    else:
        print('I Win!!')
else:
    print('Wrong choice man, try again.')
