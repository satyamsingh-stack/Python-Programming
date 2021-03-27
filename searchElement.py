from array import*
arr=array('i',[])
n=int(input("Enter the Size of the Array:"))
print("Enter the Element of the Array:")
for i in range(n):
    b=int(input())
    arr.append(b)
print(arr)
x=int(input("Enter the Element which is to be search:"))
k=0
for j in arr:
    if(j==x):
        print(k)
        break
    k=k+1