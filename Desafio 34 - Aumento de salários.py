"""
 * Project: Salary increase.
 * Objective: To calculate the salary increase.
 * Author: José Valdeir
 * Date: 08/01/2021
"""
sal = int(input('Type the salary: '))
if sal > 1250:
    sal = sal + sal*0.1
    print(f'The new salary will be {sal}')
else:
    sal = sal + sal*0.15
    print(f'The new salary will be {sal}')
