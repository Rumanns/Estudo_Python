"""
 * Project: Multiplication Table.
 * Objective: Multiplication table.
 * Author: José Valdeir
 * Date: 09/01/2021
"""
num = int(input('Digite um número: '))
for c in range(1, 11):
    print(f'{num} x {c} = {num*c}')
