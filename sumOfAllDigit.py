n=int(input("Enter the number:"))
s=0
k=n
while(n>0):
    r=n%10
    s=s+r
    n=n//10
print(s)