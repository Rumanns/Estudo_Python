"""
 * Project: Guess game.
 * Objective: Guess which number the computer is thinking.
 * Author: José Valdeir
 * Date: 08/01/2021
"""
import random
num = int(input("Welcome traveler. Come to play with me. I'll think a number in 1 until 5, guess which is!?\n"))
n = [1, 2, 3, 4, 5]
sort = random.choice(n)
print(f'I thought {sort} and you tell {num}')
if num == n:
    print('Oh my god, you hit it!')
else:
    print("You're wrong. Get out of Here")
