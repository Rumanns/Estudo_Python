"""
 * Project: Calculating Matrices.
 * Objective: Calculating Matrices.
 * Author: José Valdeir
 * Date: 18/01/2021
"""
totalrows = int(input('How many rows will have your matrix? '))
totalcolumns = int(input('How many columns will have your matrix? '))
matriz = []

for l in range(0, totalrows):
    for c in range(0, totalcolumns):
        num = input(f'Number [{l}][{c}]: ')
        matriz.append(num)

for n in range(0, len(matriz)):
    print(f'[{matriz[n]:^3}]', end=' ')
    if n >= totalcolumns-1:
        totalcolumns += totalcolumns
        print('')
