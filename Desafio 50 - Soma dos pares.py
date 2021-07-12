"""
 * Project: Sum of pairs.
 * Objective: Sum pairs.
 * Author: José Valdeir
 * Date: 10/01/2021
"""
cont = 0
soma = 0
for c in range(1, 7):
    num = int(input('Enter a number: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f'You entered {cont} even numbers and the sum of them is {soma}')
