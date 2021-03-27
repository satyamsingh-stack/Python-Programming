class Student:
    def __init__(self,n):
        self.n=n
    def factorial(self):
        f=1
        for i in range(1,n+1):
            f=f*i
        print("Factorial is",f)
if(__name__=='__main__'):
    n=int(input("Enter the Number:"))
    s1=Student(n)
    s1.factorial()