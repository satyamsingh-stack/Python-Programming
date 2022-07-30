n=int(input())
s=0
k=n
while(n):
    r=n%10
    s=s*10+r
    n=n//10
if(s==k):
    print("Pallindrome")
else:
    print("Not Pallindrome")
