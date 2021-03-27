a=0
b=1
n=int(input("Enter the number of term:"))
print(str(a))
print(str(b))
for i in range(3,n+1):
    c=a+b
    a=b
    b=c
    print(str(c))