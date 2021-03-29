def add(x,y):
    c=x+y
    print("SUM is",c)
def sub(x,y):
    d=x-y
    print("Subtraction is",d)
def multiply(x,y):
    a=x*y
    print("Multiplication is",a)
def devide(x,y):
    b=x//y
    print("Division is",b)
n=int(input("Enter the First number:"))
m=int(input("Enter the Second number:"))
q=input("Enter the symbol of Operation:")
if(q=='+'):
    add(n,m)
elif(q=='-'):
    sub(n,m)
elif(q=='*'):
    multiply(n,m)
elif(q=='/'):
    devide(n,m)
else:
    print("We are working on this operation")