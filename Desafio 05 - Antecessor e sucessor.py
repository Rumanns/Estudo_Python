'''
 * Título: Antecessor e Sucessor
 * Objetivo: Calcular o antecessor e sucessor de um determinado número.
 * Data: 18/12/2020
 * Autor: José Valdeir
'''
n1 = int(input('Digite um número: '))
ant = n1-1
suc = n1+1
print(f'O antecessor de {n1} é {ant} e o seu sucessor é {suc}')
print('-='*30,end='-\n')
print(f'Antecessor de {n1} = {ant}\n'
      f'Sucessor de {n1} = {suc}')
