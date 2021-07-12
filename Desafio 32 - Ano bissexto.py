"""
 * Project: Leap Year.
 * Objective: Verify if the year is leap or not.
 * Author: José Valdeir
 * Date: 08/01/2021
"""
year = int(input(f'Type a year: '))
if year % 4 == 0:
    print(f'The year {year} is leap.')
else:
    print(f"The year {year} isn't leap")