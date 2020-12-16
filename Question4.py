"""
Take 20 integer inputs from user and print the following:
number of positive numbers
number of negative numbers
number of odd numbers
number of even numbers
"""
lst = []
c_pos = 0 
c_neg = 0
c_odd = 0
c_even = 0 
print('Enter the elements of list : ')
for i in range(0,20):
    a = int(input())
    lst.append(a)
    if a%2 == 0:
        c_even+=1
    else:
        c_odd+=1
    if a>=0 :
        c_pos+=1
    else:
        c_neg+=1 

print('No. of Even no. : '+str(c_even))
print('No. of Odd no. : '+str(c_odd))
print('No. of Positive no. : '+str(c_pos))
print('No. of Negative no. : '+str(c_neg))
    