#CTI-110
#P2HW2 - List
#James Reynolds
#10/16/2022
#
#Prompt grades for modules 1-6
#List grades
#Display lowest grade
#Display highest grade
#Display sum of grades
#Display average of grades

module_1 = float(input('Enter grade for Module 1: '))
module_2 = float(input('Enter grade for Module 2: '))
module_3 = float(input('Enter grade for Module 3: '))
module_4 = float(input('Enter grade for Module 4: '))
module_5 = float(input('Enter grade for Module 5: '))
module_6 = float(input('Enter grade for Module 6: '))
module_grades = [module_1, module_2, module_3, module_4, module_5, module_6]
print()
print('-----------Results------------')
print('Lowest Grade:     ', min(module_grades))
print('Highest Grade:    ', max(module_grades))
print('Sum of Grades:    ', sum(module_grades))
module_grades_average = sum(module_grades) / len(module_grades)
print('Average:          ', f'{module_grades_average:.2f}')
print('----------------------------------------')
