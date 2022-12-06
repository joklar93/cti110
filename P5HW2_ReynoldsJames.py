#Adding and subtracting randomn numbers
#11-26-2022
#CTI-110 P5HW2 - Math Quiz
#James Reynolds
#
#

import random
olaf = random.randint(0, 100)
def display_intro():
    print('Welcome to my Math Quiz')
    print()

def display_main_menu():
    print('MAIN MENU')
    print('--------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print()

def menu_option():
    user_option = int(input('Please choose one of the menu options: '))
    if user_option < 1 or user_option > 3: 
        print()
        print('Error')
        print()
        display_main_menu()
        user_option = int(input('Please choose one of the menu options: '))
    return user_option
    
def add_rng_num():
    count = 1
    print(' ', rng1)
    print('+', rng2)
    print()
    print('Enter answer.')
    user_guess = int(input())
    while user_guess != rng_add:
        if user_guess > rng_add:
            print('Sorry, guess is too high.')
            print()
            count += 1
            user_guess = int(input('try again: '))
        if user_guess < rng_add:
            print('Sorry, guess is too low.')
            print()
            count += 1
            user_guess = int(input('try again: '))
    
    print('Congratulations!!!! your answer is correct..')
    print(f'Number of guesses: {count}')
    print()
    display_main_menu()

def sub_rng_num():
    count = 1
    print(' ', rng1)
    print('-', rng2)
    print()
    print('Enter answer.')
    user_guess = int(input())

    while user_guess != rng_sub:
        if user_guess > rng_sub:
            print('Sorry, guess is too high.')
            print()
            count += 1
            user_guess = int(input('try again: '))
        if user_guess < rng_sub:
            print('Sorry, guess is too low.')
            print()
            count += 1
            user_guess = int(input('try again: '))
  
    print('Congratulations!!!! your answer is correct..')
    print(f'Number of guesses: {count}')
    print()
    display_main_menu()
        
def exit_math_quiz():    
    print('Thank you for playing...')
    print('Bye!!')
    
    
def math_quiz():
    global rng1, rng2, rng_add, rng_sub
    display_intro()
    display_main_menu()
    option = menu_option()    
    while option > 0 and option < 4:
        rng1 = random.randint(1, 99)
        rng2 = random.randint(1, 99)
        if option == 1:
            rng_add = rng1 + rng2
            add_rng_num()
            option = menu_option()
        elif option == 2:
            rng_sub = rng1 - rng2
            sub_rng_num()
            option = menu_option()
        else:
            exit_math_quiz()
            break
        
         
        
        
        
            
math_quiz()
    

