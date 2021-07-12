"""
 * Project: Approving Loan.
 * Objective: Verify if a loan is approved.
 * Author: José Valdeir
 * Date: 08/01/2021
"""
house = input('What is the value of the house? ')
sal = input('What is your salary: ')
years = input('How old would you like to pay? ')

months = years*12
installment = house/months

if installment >= sal(30/100):
    print('Financing not approved')
else:
    print('Financing approved with success! Congratulations!')
