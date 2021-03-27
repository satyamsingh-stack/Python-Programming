a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
d=int(input("Enter the fourth number:"))
if(a>b and a>c and a>d):
    print(str(a)+ "is the largest number")
elif(b>a and b>c and b>d):
    print(str(b)+ "is the largest number")
elif(c>a and c>b and c>d):
    print(str(c)+ "is the largest number")
else:
    print(str(d)+ "is the largest number")