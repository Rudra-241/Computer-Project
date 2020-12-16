"""
Write a prog in Python, which should count and display the occurrence of
alphabets A and M (including small cases a and m too) in a string.
prog should display the output as:
A or a:4
M or m :2"""
s = input('Enter the string : ').lower()
ca = list(s).count('a')
cm = list(s).count('m')
print('A or a : '+str(ca))
print('M or m :'+str(cm))