def insertion_sort(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while(j>=0 and l[j]>key):
            l[j+1]=l[j]
            j=j-1
        l[j+1]=key
    return l
l=[55,44,33,22,11]
ans=insertion_sort(l)
print(ans)