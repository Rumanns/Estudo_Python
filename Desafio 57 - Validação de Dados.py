"""
 * Project: Sex validation
 * Objective: Sex validation
 * Author: José Valdeir
 * Date: 10/01/2021
"""
sexo = ' '
while sexo not in 'FfMm':
    sexo = str(input('Wrong choice. Try again.\nSex? [M/F] ')).upper()
if sexo == 'M':
    sexo = 'Male'
if sexo == 'F':
    sexo = 'Female'
print('The sex is {}.'.format(sexo))
