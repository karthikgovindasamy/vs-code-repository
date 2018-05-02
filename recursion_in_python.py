"""
This is recursion in python
"""

def factorial(n):
    """
    This function computes factorial recursively
    """
    if n==1:
        return 1
    else:
        return n*factorial(n-1)


#test code
print 'factorial of 15 is {}'.format(factorial(15))
print 'factorial of 5 is {}'.format(factorial(5))
print 'factorial of 9 is {}'.format(factorial(9))