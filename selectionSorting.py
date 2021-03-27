# def sort(l):
#     for i in range(0,n-1):
#         minpos=i
#         for j in range(i,n+2):
#             if(l[j]<l[minpos]):
#                 minpos=j
#         temp=l[i]
#         l[i]=l[minpos]
#         l[minpos]=temp
# l=[]
# n=int(input("Enter size:"))
# for i in range(n):
#     a=int(input())
#     l.append(a)
# print(l)
# sort(l)
# print("After sorting",l)


l=[1,4,2,3,6,0,3]
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if(l[i]>l[j]):
            l[i],l[j]=l[j],l[i]
for i in range(len(l)):
    print(l[i],end=" ")