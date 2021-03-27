a=int(input("Enter divider:"))
b=int(input("Enter divisor:"))
try:
    print("Resourses Open")
    if(a>b):
        x=a//b
        print(x)
    else:
        x=b//a
        print(x)
    k=int(input("Enter a number:"))
    print(k)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception:
    print("Something went Wrong...")
finally:
    print("Resourses Closed")