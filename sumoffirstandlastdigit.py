def reverse(n):
    s=0
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    return s%10
t=int(input())
s=0
for i in range(t):
    n=int(input())
    last=n%10
    first=reverse(n)
    s=last+first
    print(s)