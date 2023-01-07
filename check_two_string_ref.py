"""
Write a python script to input two strings from the user and display whether the two
variables referred to the same object or not. Print True or False
"""

# taking two string from the user
str1, str2 = input("Enter First String : "), input("Enter Second String : ")

# checking two stringtwo variables referred to the same object or not
# using identity operator - 'is'
if str1 is str2:
    print("True")
else:
    print("False")
    
# single line if-else
# print("True" if str1 is str2 else "False")