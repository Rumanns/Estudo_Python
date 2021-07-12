"""
 * Project: Fibonacci.
 * Objective: Show terms of Fibonacci sequence.
 * Author: José Valdeir
 * Date: 10/01/2021
"""
print('-'*30)
print('Fibonacci Sequence')
print('-'*30)
num = int(input('How many terms in this sequence do you want to see?\n'))
t1 = 0
t2 = 1
print('{}\n{}'.format(t1, t2))
termos = 3
while termos < num:
    t3 = t1 + t2
    print('{}'.format(t3))
    termos += 1
    t1 = t2
    t2 = t3
print('End')
