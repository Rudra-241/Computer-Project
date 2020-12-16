"""
Write a prog that read a tuple and print the maximum number from the tuple.
"""
lst = []
n = int(input('No. of elements : '))
print('Enter some elements ')
for i in range(0,n):
    a= int(input())
    lst.append(a)
tupl = tuple(lst)
m = max(tupl)
print('Maximum integer in the tuple is : '+str(m))