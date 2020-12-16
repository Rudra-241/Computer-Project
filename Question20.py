"""
Write a program to generate random numbers between 1 to 6 and check
whether a user won a lottery or not.
"""
import random
rand_int = random.randint(1,6)
num = int(input('Enter any number in between 1 to 6 : '))
if num == rand_int:
    print('You won the lottery')
else:
    print('You didn\'t won the lottery')
