"""
Write a program that asks the user how many Fibonnaci numbers to
generate and then generates them.
"""
n = int(input('Enter no. of terms of Fibonnaci numbers '))
a = 0
b = 1
for i in range(0,n):
    print(a)
    sum = a+b
    a = b 
    b = sum