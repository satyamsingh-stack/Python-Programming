n=int(input())
k=n
s=0
while(n>0):
    r=n%10
    s=s+(r*r*r)
    n=n//10
if(k==s):
    print("Armstrong")
else:
    print("Not Armstrong")