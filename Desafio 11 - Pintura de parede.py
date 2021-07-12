'''
 * Projeto: Pintura de parede
 * Objetivo: Calculo do tamanho de uma parede
 * e o tanto de tinta necessário para pintá-la,
 * sabendo que cada litro de tinta pinta 2m².
 * Autor: José Valdeir
 * Data: 18/12/2020
'''
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
A = altura*largura
total = A/2
print(f'O total de tinta para necessário para pintar a parede é {total:.3f} litros de tinta')
