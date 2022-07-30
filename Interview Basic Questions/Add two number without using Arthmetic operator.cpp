a,b=int(input()),int(input())
while(b!=0):
    temp=a&b
    a=a^b
    b=temp>>1
print(a)
