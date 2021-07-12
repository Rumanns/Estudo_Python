'''
 * Projeto: Aumento de Salário
 * Objetivo: Calcula um salario com 15% de aumento.
 * Autor: José Valdeir
 * Data: 18/12/2020
'''
sal = int(input('Digite o salário: '))
aumento = sal*15/100
total = sal+aumento
print(f'O aumento do salário é de {aumento:.2f}\n'
      f'O total do salário com aumento é {total:.2f}')
