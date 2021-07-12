"""
 * Project: Calculating Matrices Determinant.
 * Objective: Calculating Matrices Determinant.
 * Author: José Valdeir
 * Date: 18/01/2021
"""
totalrows = int(input('How many rows will have your matrix? '))
totalcolumns = int(input('How many columns will have your matrix? '))
matriz = []
squareMatrix = bool

diagonalP = []

for l in range(0, totalrows):
    for c in range(0, totalcolumns):
        num = input(f'Number [{l}][{c}]: ')
        matriz.append(num)
        if c == l:
            diagonalP.append(num)

if totalrows == totalcolumns:
    squareMatrix = True

for n in range(0, len(matriz)):
    print(f'[{matriz[n]:^3}]', end=' ')
    if n >= totalcolumns-1:
        totalcolumns += totalcolumns
        print('')

if squareMatrix:
    print(f'The matrix is square and has determinant!')
    print(f'The main diagonal is {diagonalP}')
