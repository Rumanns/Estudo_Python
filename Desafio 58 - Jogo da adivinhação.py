"""
 * Project: Guess game
 * Objective: Guess game
 * Author: José Valdeir
 * Date: 10/01/2021
"""
from random import randint
num = int(input("I'm thinkin of a number from 0 to 10, guess what it is: \n"))
computador = randint(0, 10)
while computador != num:
    num = int(input('Wroooong! Try again: '))
print('You hit it! Congratulations!!! \o/')
