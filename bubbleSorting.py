def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if(nums[j]>nums[j+1]):
                t=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=t
nums=[]
n=int(input("Enter size of the lst:"))
print("Element of the lst")
for i in range(n):
    a=int(input())
    nums.append(a)
print(nums)
sort(nums)
print("After sorting",nums)


# l=[2,7,1,9,7]
# for i in range(0,len(l)-1):
#     for j in range(0,len(l)-i-1):
#         if(l[j]>l[j+1]):
#             l[j],l[j+1]=l[j+1],l[j]
# for i in range(len(l)):
#     print(l[i],end=" ")