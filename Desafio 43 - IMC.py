"""
 * Project: BMI
 * Objective: Calculate the BMI (Body Mass Index)
 * Author: José Valdeir
 * Date: 09/01/2021
"""
import math
mass = int(input('Enter the mass in kilograms: '))
height = int(input('Enter the height in centimeters: '))
bms = mass/((height**2)/10000)
print(f'Your BMS is {bms:.3f}')

if bms < 18.5:
    print('Under weight.')
elif 18.5 < bms < 25:
    print('Ideal weight')
elif 25 < bms < 30:
    print('overweight')
elif 30 < bms:
    print('Morbid obesity')
