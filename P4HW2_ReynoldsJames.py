#CTI-110
#P4HW2
#Reynolds
#11/15/2022
#Salary Calculator
#
#While name != "None"
#   prompt name, hours_worked, pay_rate   
#   Calculate over_time, over_time_pay, reg_pay, gross_pay
#   Print hours_worked, pay_rate, over_time, over_time_pay, regular_pay, and gross_pay
#   If statement for overtime and overtime pay for decimals
#   Calculate count, total_overtime, total_hour_pay, gross_total
#Print count
#Print total_overtime
#Print total_hour_pay
#Print gross_total

total_overtime = 0
total_hour_pay = 0
gross_total = 0
count = 0
name = input('Enter employee\'s name or "None" to terminate: ')
while name != 'None':
    hours_worked = float(input(f'How many hours did {name} work? '))
    pay_rate = float(input(f'What is {name} workpay rate? '))

    over_time = hours_worked - 40
    
    if  hours_worked-40 <= 0:
        over_time = 0
    elif hours_worked > 40:
        over_time = hours_worked-40

    if over_time > 0:
        over_time_pay = over_time*pay_rate*1.5
    elif over_time <= 0:
        over_time_pay = 0
        
    
    reg_pay = pay_rate*(hours_worked-over_time)
    gross_pay = reg_pay+over_time_pay
    
    print()
    print(f'Employee name:   {name}')
    print()
    print('Hours Worked   Pay Rate    OverTime     OverTime Pay       RegHour Pay         Gross Pay')
    print('----------------------------------------------------------------------------------------------------')
    if over_time <= 0:
        print(f'{hours_worked:<15.1f}{pay_rate:<12.1f}{over_time:<13.0f}{over_time_pay:<19.0f}${reg_pay:<20.2f}${gross_pay:.2f}')
    elif over_time > 0:
        print(f'{hours_worked:<15.1f}{pay_rate:<12.1f}{over_time:<13.1f}{over_time_pay:<19.2f}${reg_pay:<20.2f}${gross_pay:.2f}')
    print()
            
    
    count += 1
    total_overtime = total_overtime + over_time_pay
    total_hour_pay = total_hour_pay + reg_pay
    gross_total = total_overtime + total_hour_pay
    
    name = input('Enter employee\'s name or "None" to terminate: ')
    
print()
print(f'Total number of employees entered:{count}')
print(f'Total amount payed for overtime: ${total_overtime:.2f}')
print(f'Total amount payed for regular hours: ${total_hour_pay:.2f}')
print(f'Total amount payed in gross: ${gross_total:.2f}')
    
    





    
