def linear(l,key):
    for i in range(len(l)):
        if(l[i]==key):
            return i
    return -1
n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
key=int(input())
ans=linear(l,key)
if(ans==-1):
    print("Element Not Found")
else:
    print(f"Element Found at index : {ans}")