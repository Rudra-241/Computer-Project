"""
Write a program to calculate simple interest
"""
P = float(input('Enter Principal Value : '))
R = float(input('Enter Rate% : '))
T = float(input('Enter Time Period : '))
SI = (P * R * T)/100 
print("SI : "+str(SI))