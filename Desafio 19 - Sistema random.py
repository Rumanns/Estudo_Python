'''
 * Project: Name Random.
 * Objective: To select a random name in five names.
 * Author: José Valdeir
 * Date: 07/01/2021
'''
import random

nome = ['Alceu', 'Fagner', 'Zé', 'Ivete', 'Elba']
sort = random.randint(0, 4)
print(nome[sort])
