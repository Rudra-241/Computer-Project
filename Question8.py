"""
Write a program to input a character and to print whether a given character
is an alphabet, digit or any other character.
"""
a = (input('Enter the character : '))[0]
if a.isalpha():
    print('Alphabet')
elif a.isdigit():
    print('Digit')
else:
    print('Any other Symbol')
