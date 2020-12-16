"""
Write a python code to find length of a string without using len( ) function.
"""
s = input('Enter the String : ')
length = 0 
for ch in s :
    length+=1
print('Length is ',length)