n=int(input())
s=0
k=n
while(n):
    r=n%10
    s=s+(r*r*r)
    n=n//10
print(s==k)
