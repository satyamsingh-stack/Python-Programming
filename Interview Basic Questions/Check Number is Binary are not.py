n=int(input())
def check(n):
    while(n):
        r=n%10
        if(r!=0 and r!=1):
            return False
        n=n//10
    return True
print(check(n))
