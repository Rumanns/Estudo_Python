"""
 Title: Lottery
 Objective: Randomize numbers to play lottery.
 Author: José Valdeir
"""
from random import randint
from time import sleep

jog = list()
tot = list()
nums = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, nums):
    for n in range(0, 6):
        nur = randint(1, 60)
        while nur in jog:
            nur = randint(1, 60)
        jog.append(nur)
    jog.sort()
    tot.append(jog[:])
    jog.clear()

for i, l in enumerate(tot):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
