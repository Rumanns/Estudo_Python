'''
 * Project: Name Random.
 * Objective: To select a random name in five names.
 * Author: José Valdeir
 * Date: 07/01/2021
'''
import random

n1 = input('Type the name 1: ')
n2 = input('Type the name 2: ')
n3 = input('Type the nome 3: ')
n4 = input('Type the name 4: ')

nomes = [n1, n2, n3, n4]
random.shuffle(nomes)
print(nomes)
