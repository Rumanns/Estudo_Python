"""
 * Project: Multiple of 3.
 * Objective: Verify multiples of 3.
 * Author: José Valdeir
 * Date: 09/01/2021
"""
soma = 0
cont = 0
n1 = int(input('Enter a number: '))
n2 = int(input('Enter other number: '))
for c in range(n1, n2, 3):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
        print(c, end = ' ')
print(f'\nThe end. Are {cont} sums and the total is {soma}')
