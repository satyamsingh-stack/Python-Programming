lst1=[]
lst2=[]
lst3=[]
n=int(input("Enter the size:"))
print("Enter the element of first list:")
for i in range(n):
    a=int(input())
    lst1.append(a)

print("Enter the element of second list:")
for i in range(n):
    b=int(input())
    lst2.append(b)

for i in range(n):
    lst3.append(lst1[i]+lst2[i])
print(lst3)