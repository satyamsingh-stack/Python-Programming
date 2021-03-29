a=float(input("Enter the first side of the triangle:"))
b=float(input("Enter the second side of the triangle:"))
c=float(input("Enter the third side of the triangle:"))
if(a==b and a==c and b==c):
    print("EQUILATERIAL Triangle")
elif(a!=b and a!=c and a!=b):
    print("SCALANE Triangle")
elif((a==b and b!=c) or (b==c and c!=a) or (c==a and a!=b)):
    print("ISOCALES Triangle")