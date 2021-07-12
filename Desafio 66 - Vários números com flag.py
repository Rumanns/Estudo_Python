"""
 * Project: Numbers with flag.
 * Objective: Numbers sum with flag.
 * Author: José Valdeir
 * Date: 10/01/2021
"""
cont = soma = 0
while cont != 999:
    cont += 1
    num = int(input('Enter a number: '))
    soma += num
    if num == 999:
        break
    num += num
print('The total of numbers was: {}\n'
      'And their sum is: {}'.format(cont-1, soma-999))
