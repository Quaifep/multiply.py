# Author: Paul Quaife
# Date: 2/4/2021
# Description: Recursive function that takes two positive integers as parameters
# and returns the product of those two numbers

def multiply(a, b):
    """function that takes two positive integers as parameters
# and returns the product of those two numbers"""
    if a == 0:
        return 0
    else:
        return b+multiply(a-1, b)
