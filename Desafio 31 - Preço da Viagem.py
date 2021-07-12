"""
 * Project: Travel price.
 * Objective: To calculate the price of an travel.
 * Author: José Valdeir
 * Date: 08/01/2021
"""
miles = int(input('Type the distance of destination: '))
if miles <= 200:
    total = miles/2 # or: total = miles*0.5
    print(f'The total is {total:.3f}')
else:
    total = miles/2.222 # or: total = miles*0.45
    print(f'The total is {total:.3f}')
