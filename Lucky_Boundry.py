t=int(input())
for i in range(t):
    n=int(input())
    s=0
    for m in range(1,n+1):
        if(n%m<=n/2):
            s=s+1
    print(s)
