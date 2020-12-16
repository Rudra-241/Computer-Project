"""
Write a python prog that calculate compound interest.
"""
P = float(input('Enter Principal Amount : '))
r = float(input('Enter Rate% : '))
n = float(input('Enter time period : '))

amount = P*(1+(r/100))**n
CI = amount-P 
print('Amount :'+str(amount))
print('Compound Interest :'+str(CI))