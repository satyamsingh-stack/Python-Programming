from math import sqrt
x2=int(input("Enter the value of second point of x axis:"))
y2=int(input("Enter the value of second point of y axis:"))
x1=int(input("Enter the value of first point of x axis:"))
y1=int(input("Enter the value of first point of y axis:"))
d=sqrt(pow((x2-x1),2)+pow((y2-y1),2))
print("The distance between these two point is:"+str(d))