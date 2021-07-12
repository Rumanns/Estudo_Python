"""
 * Project: Separating vowels
 * Objective: Separating vowels
 * Author: José Valdeir
 * Date: 10/01/2021
"""
palavras = ('SOFISTICADO', 'MALICIA', 'MAE','IRMA','AMOR','PAZ','SEGURANÇA',
            'NAMORO','APRENDER','EVOLUIR','AJUDAR','HAMONIA')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end='')
