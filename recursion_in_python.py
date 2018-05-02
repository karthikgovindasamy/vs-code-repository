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

def fibonacci(n):
    if n<2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


#test code
print 'factorial of 15 is {}'.format(factorial(15))
print 'factorial of 5 is {}'.format(factorial(5))
print 'factorial of 9 is {}'.format(factorial(9))
print fibonacci(3)
print fibonacci(8)
print fibonacci(2)
print fibonacci(15)
print fibonacci(18)