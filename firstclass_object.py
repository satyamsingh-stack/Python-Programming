def factorial(n):
    """this is Satyam Singh"""
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial.__doc__)