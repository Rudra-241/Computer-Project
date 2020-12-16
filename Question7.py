"""
Ask user to give integer inputs to make a list. Store only even values given
and print the list.
"""
lst = []
n = int(input('Enter the number of Elements : '))
print('Enter Elements ')
for i in range(0,n):
    a = int(input())
    if a%2 == 0:
        lst.append(a)
print('Your list of Even Numbers',lst)