def isprime(n):
    for i in range(2,int(n**1/2)+1):
        if(n%i==0):
            return False
    return True

n=int(input())
print(isprime(n))
