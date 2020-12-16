"""
Write a Python function to create and print a list where the values are square
of numbers between 1 and 20 (both included).
"""
lst = []
def main():
    for i in range(1,21):
        lst.append(i*i)
        
    print('The list is :',lst)
main()