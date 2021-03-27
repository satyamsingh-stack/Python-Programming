def fib(n):
    a=0
    b=1
    if(n==1):
        print(a)
    elif(n==2):
        print(a)
        print(b)
    elif(n<0):
        print("Wrong Input")
    elif(n==0):
        print("Please enter number more than 0")
    else:
        print(a)
        print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
n=int(input("Enter the Number:"))
fib(n)