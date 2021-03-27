n=int(input())
l1=[]
for i in range(n):
    a=int(input())
    l1.append(a)
print(l1)
max=l1[0]
second_max=l1[0]
for i in range(n):
    if(l1[i]>max):
        second_max=max
        max=l1[i]
    elif(l1[i]<max and l1[i]>second_max):
        second_max=arr[i]
print(second_max)