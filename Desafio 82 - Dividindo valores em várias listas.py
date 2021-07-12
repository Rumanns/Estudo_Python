"""
 * Project: Relating lists.
 * Objective: Separate values in multiple lists.
 * Author: José Valdeir
 * Date: 13/01/2021
"""
nomes = []
idades = []
continuar = 'S'
while True:
    nome = input('Enter a name: ')
    if nome in nomes:
        print('The name already in list. Input other name.')
    else:
        nomes.append(nome)
        idades.append(int(input('Enter age: ')))

    continuar = input('Do you want to continue? [S][N]').upper()
    if continuar == 'N':
        break

for n in range(0, len(nomes)):
    print(f'{nomes[n]:-<10}{idades[n]:5}')
