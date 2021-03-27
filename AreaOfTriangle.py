from math import sqrt
a=int(input("Enter the first side of the triangle:"))
b=int(input('Enter the second side of the triangle:'))
c=int(input("Enter the third side of the triangle:"))
s=(a+b+c)/2
area=sqrt((s-a)*(s-b)*(s-c))
print("The Area Of the Triangle is:"+str(area))


