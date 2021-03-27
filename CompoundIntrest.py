p=int(input("Enter the value of p:"))
r=int(input("Enter the value of r:"))
t=int(input("Enter the value of t:"))
a=p*pow((1+(r/100)),t)
CI=a-p
print("The COMPOUND INTREST is:"+str(CI))