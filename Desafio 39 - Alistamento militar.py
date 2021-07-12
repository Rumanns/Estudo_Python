"""
 * Project: Military enlistment.
 * Objective: Check if the person is able to enlist.
 * Author: José Valdeir
 * Date: 08/01/2021
"""
age = int(input(f'Type the age: '))
if age < 18:
    print(f'You cannot enlist. {18-age} years to go.')
elif age == 18:
    print(f'Is time to enlist! "Go mongo go!"')
elif 18 < age < 26:
    print(f'Still time to enlist!')
else:
    print(f'You can no long enlist. Is late. {age-25} years passed.')
