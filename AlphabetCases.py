c=int(input("Enter the letter:"))
if(c>=65 and c<=70):
    print("UPPER CASE")
elif(c>=97 and c<=122):
    print("lower case")
elif(c>=48 and c<=57):
    print("Number")
else:
    print("Special Character")