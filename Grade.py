a=float(input("Enter the Maths no:"))
b=float(input("Ener the English no:"))
c=float(input("Enter the Physics no:"))
d=float(input("Enter the Chemistery no:"))
e=float(input("Enter the Optional subject no:"))
sum=(a+b+c+d+e)
print("Total no:"+str(sum))
p=sum/5
print("You got:  "+str(p)+'%')
if(p>=91 and p<=100):
    print("You Got 'A' Grade")
elif(p>=81 and p<=90):
    print("You got 'B' Grade")
elif(p>71 and p<=80):
    print("You got 'C' Grade")
elif(p>61 and p<=70):
    print("You got 'C' Grade")
elif(p>=51 and p<=60):
    print("You got 'D' Grade")
else:
    print("You are failed and got 'E' Grade")