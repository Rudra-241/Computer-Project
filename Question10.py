"""
Write a prog to read an integer list and print sum of the list
"""
lst = []
sum = 0 
n = int(input('Enter no. of terms of list : '))
print('Enter the elements ')
for i in range(0,n):
    a = int(input())
    sum+=a
    lst.append(a)
print('Sum is '+str(sum))