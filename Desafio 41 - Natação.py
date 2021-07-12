"""
 * Project: Swimming Class
 * Objective: Swimming class organization.
 * Author: José Valdeir
 * Date: 09/01/2021
"""
byear = int(input('Enter year birth: '))
cyear = int(input('Enter the current year: '))
age = byear - cyear

if age < 10:
    print('Child class I')
elif age < 15:
    print('Child class II')
elif age < 20:
    print('Junior class')
elif age < 21:
    print('Senior class')
else:
    print('Master')
