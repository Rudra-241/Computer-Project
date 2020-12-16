"""
Write a prog that convert temperature form Celsius to Fahrenheit and
Fahrenheit to Celsius
"""
choice = int(input("Enter 1 for Fahrenheit to Celsius\nEnter 2 for Celsius to Fahrenheit\n"))
if choice == 1:
    f = float(input('Enter temperature in Fahrenheit: '))
    c = (f-32)*5/9
    print(c,' Celsius',end = '')
elif choice == 2:
    c = float(input('Enter temperature in Celsius: '))
    f = (c*9/5)+32
    print(f,' Fahrenheit',end = '')
else:
    print('INVALID CHOICE')
