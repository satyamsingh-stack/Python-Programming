from functools import reduce
nums=[]
a=int(input("Enter the Size of the List:"))
print("Enter the Element of the list:")
for i in range(a):
    b=int(input())
    nums.append(b)
print(nums)

evens=list(filter(lambda n:n%2==0,nums))
print(evens)

doubles=list(map(lambda n: n+2,evens))
print(doubles)

red=reduce(lambda c,d:c+d,nums)
print(red)