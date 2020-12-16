"""
Write a Python program to multiply all the items in a dictionary.
"""
dict = {}
n = int(input('Enter no. of elements : '))
for i in range (0,n):
    dict[i] = int(input('Enter element\n'))

p=1
for key in dict:    
    p=p * dict[key]

print(p)