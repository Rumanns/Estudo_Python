"""
 * Project: School Average
 * Objective: Calculate the media of school
 * Author: José Valdeir
 * Date: 08/01/2021
"""
grade1 = int(input('Type the first grade: '))
grade2 = int(input('Type the second grade: '))
average = (grade1+grade2)/2

if average == 0:
    print('Disapproved.')
elif 0 < average < 7:
    print('Educational recovery. Try again.')
elif 7 < average < 11:
    print('Approved! Congratulations!')
