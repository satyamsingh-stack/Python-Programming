n,a=map(int,input().split(','))
k=n
s=1
while(k>0):
    r=k%10
    s=s*r
    k=k//10
s=s*n
if(s==a):
    print(True)
else:
    print(False)