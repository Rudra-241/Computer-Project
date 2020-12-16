"""
Write a Python program to check whether an element exists within a tuple.
"""
lst = []
n = int(input('No. of elements : '))
ele = (input('Enter the Element : '))
print('Enter some elements ')
for i in range(0,n):
    a= input()
    lst.append(a)
tupl = tuple(lst)
if ele in tupl :
    print('Yes,it is present')
else:
    print('No,it is not present')
