"""
Write a program to calculate the factorial of an integer.
"""
a = int(input('Enter the integer : '))
fact = 1
for i in range(1,a+1):
    fact*=i
print('Factorial is '+str(fact))