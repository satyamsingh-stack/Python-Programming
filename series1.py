from math import pow
n=int(input("Enter the number of term:"))
s=0
for i in range(1,n+1,+2):
    s=s+pow(i,i)
    print(s)