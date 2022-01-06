'''
 * Título: Tipo de variável
 * Objetivo: Testar o tipo de variável de diversas formas.
 * Data: 18/12/2020
 * Autor: José Valdeir
'''
v = str(input('Digite algo: '))
print(f'O tipo dessa variável é {type(v)}')
print(f'O tipo de {v} é {type(v)}'
      f'\n {v} é {v.isnumeric()} para número'
      f'\n {v} é {v.isalpha()} para letra'
      f'\n {v} é {v.lower()} para minúsculas')
