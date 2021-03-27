from functools import reduce
n=int(input())
a=reduce(lambda x,y:x*y,range(1,n+1))
print(a)