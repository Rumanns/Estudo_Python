"""
 * Project: Shopping list.
 * Objective: Shopping list on tuplas
 * Author: José Valdeir
 * Date: 10/01/2021
"""
itens = ('Pencil', 1.00,
         'Pen', 1.00,
         'Rubber', 1.50,
         'Automatic pencil',9.00,
         'Colored pencil', 15.00,
         'White Sheet', 20.00)
print('-'*40)
print(f'{"Shopping List":^40}')
print('-'*40)
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}',end='')
    if pos % 2 == 1:
        print(f'R$ {itens[pos]:>}')
