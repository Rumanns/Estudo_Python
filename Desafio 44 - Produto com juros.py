"""
 * Project: Calculating Interest.
 * Objective: Calculate Interest.
 * Author: José Valdeir
 * Date: 09/01/2021
"""
value = int(input('Enter the product value: '))
print('Choose the payment method:\n'
      '[1] Cash or check;\n'
      '[2] Card;\n'
      '[3] 2x on card;\n'
      '[4] 3x or more on card;\n')
pag = int(input('Type your option: '))
if pag == 1:
    value = value - value*10/100
    print(f'The total in cash or check is R${value}')
elif pag == 2:
    value = value - value*5/100
    print(f'The total in sight is R${value} ')
elif pag == 3:
    print(f'The total in 2x on card is R${value}')
elif pag == 4:
    value = value + value*20/100
    print(f'The total in 3x on card is R${value}')
else:
    print('Wrong choice, try again:')
