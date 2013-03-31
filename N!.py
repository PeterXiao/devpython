__author__ = 'Peter xiao'
def factorial(x):
    if  x <= 1:
        return  1
    return x * factorial(x-1)
print(factorial(10))