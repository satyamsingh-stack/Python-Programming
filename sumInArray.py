a=[]
s=0
n=int(input("Enter the size of the Array:"))
print("Enter the array element:")
for i in range(n):
    n=int(input())
    a.append(n)
print("Sum of the number is",sum(a))
av=sum(a)/n
print("Avrage of the number is",av)