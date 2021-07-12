'''
 * Projeto: Calculo de desconto
 * Objetivo: Calcular o desconto de 5% em uma mercadoria.
 * Autor: José Valdeir
 * Data: 18/12/2020
'''

preço = float(input('Digite o valor da mercadoria: '))
desconto = preço*(5/100)
total = preço - desconto
print(f'O valor do desconto é {desconto:.3f}\n'
      f'O total com desconto é {total:.3f}')
