def merg(left,right):
    result=[]
    i,j=0,0
    while(i<len(left) and j<len(right)):
        if(left[i]<=right[j]):
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
    result=result+left[i:]
    result=result+right[j:]
    return result
def mergsort(l):
    if(len(l)<=1):
        return l
    mid=int(len(l)/2)
    left=mergsort(l[:mid])
    right=mergsort(l[mid:])
    return merg(left,right)
l=[1,4,2,6,3,7]
print(mergsort(l))