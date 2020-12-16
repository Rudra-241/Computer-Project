"""
Write a Python program to calculate the average value of the numbers in a
given tuple of tuples.
"""
lst = []
n = int(input('Enter size of outer tuples:\n'))
for i in range(0,n):
    lst2 = []
    n2 = int(input('Enter size of inner tuple\n'))
    for j in range(0,n2):
        a = int(input('Enter element\n'))
        lst2.append(a)
    lst.append(tuple(lst2))
tupl = tuple(lst)
        
s = 0 
l = 0
for tup in tupl:
    s+= sum(list(tup))
    l+= len(tup)
avg = s/l
print(avg)