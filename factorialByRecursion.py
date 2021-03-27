def fact(n):
    if(n==0):
        return 1

    return n* fact(n-1)

n=int(input("Enter the Number:"))
result=fact(n)
print(result)
