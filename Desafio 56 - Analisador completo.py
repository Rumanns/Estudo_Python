"""
 * Project: Poor registration.
 * Objective: Poor registration.
 * Author: José Valdeir
 * Date: 10/01/2021
"""
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):
    print('-----{}° Person-----'.format(p))
    nome = str(input('Name: ')).strip()
    idade = int(input('Age: '))
    sexo = str(input('Sex: [M/F]')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('The average age of the group is {}'.format(mediaidade))
print('The older man is {} years old. And his name is {}'.format(maioridadehomem, nomevelho))
print('Altogether they are {} woman under 20 years old.'.format(totmulher20))
