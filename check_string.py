"""
Write a python script to print True if the string 'my' is a member in a 
String entered by the user
"""

# taking string from the user
usr_str = input("Enter a string : ")

# checking is 'my' is is a member in a string or not
# using membership operator - 'in'
if 'my' in usr_str:
    print("True")

# single line if-else
# print("True" if 'my' in usr_str else "False")
