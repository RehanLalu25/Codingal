def factorial(x):
    '''this is a recursive function'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print(factorial(2))
print(factorial(5))
