#!/usr/bin/env python3

""" This program is a simple multiplication game (12 times tables).
    The code will greet the user, then ask them multiplication questions.
    It will also give them a result of how they went, when the user quits
    out of the of the program using the letter q or Q.

    Coded by Craig
"""

import math
import random

user_input  = 0
num1        = 0
num2        = 0
counter     = 0
correct_ans = 0


def is_input_digits(inputval):
    if(inputval.isdigit()):
        return True
    return False


#############
# Main
#############

name = input("Please enter your name: ")
print(f'\nHello {name}, nice to meet you. This is a simple maths multiplication game.')
print("Please answer each question and then press the <enter> key. You will be told if you have answered the question correctly.")
print("Once you have had enough, press the letter q or Q and then press the <enter> key to quit the questions.\n")


while True:
    num1 = random.randint(1,12)
    num2 = random.randint(1,12)

    user_input = (input(f'what is {num1} x {num2}\n'))

    if (user_input == "q" or user_input == "Q"):
        percentage_correct = (correct_ans / counter) * 100
        print(f'You got {correct_ans} out of {counter} or {percentage_correct}% correct')
        if(percentage_correct > 80):
            print(f'Great effort {name}!!!')
        break

    answer = num1 * num2

    if (is_input_digits(user_input) == True):
        user_input = int(user_input)

        if (answer == user_input):
            correct_ans += 1
            print("Your answer was correct!!!\n")
        else:
            print("Your answer was incorrect.\n")
            print("NextQuestion\n")
        counter += 1
    else:
        print("What you entered was not an integer. Please try again\n")
