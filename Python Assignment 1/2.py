"""
. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order
with a space between first name and last name.
"""

a = input(" Please enter your first name:")
b = input(" please enter your last name:")
a = a[::-1]
b = b[::-1]
print( a," ",b)