"""
 * Project: Banking Cash Simulator
 * Objective: Banking Cash Simulator
 * Author: José Valdeir
 * Date: 10/01/2021
"""
print('='*30)
print('{:^30}'.format('Bank'))
print('='*30)
valor = int(input('Enter the value: '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'THe total is: {totcéd} ballot of {céd} R$')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        totcéd = 0
        if total == 0:
            break
print('='*30)
print('This is it. Check back often')
