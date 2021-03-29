n,k=map(int,input().split())
l1=[]
for i in range(n):
    a=int(input())
    l1.append(a)
x=max(l1)
ans=x-k
if(ans>0):
    print(ans)
else:
    print(0)