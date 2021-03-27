def binary(l,key):
    beg=0
    end=len(l)-1
    mid=0
    while(beg<=end):
        mid=(beg+end)//2
        if(key<l[mid]):
            end=mid-1
        elif(key>l[mid]):
            beg=mid+1
        else:
            return mid
    return -1
l=[1,2,3,4]      #Element of list should be sorted order
key=4
ans=binary(l,key)
if(ans!=-1):
    print(f"Element Found at index:{ans}")
else:
    print("Element not found")