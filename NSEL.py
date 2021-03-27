def NGE(arr,n):
    s=[]
    v=[]
    for i in range(0,n):
        while(len(s)!=0 and s[-1]>=arr[i]):
            s.pop()
        if(len(s)==0):
            v.append(-1)
        else:
            v.append(s[-1])
        s.append(arr[i])
    # v.reverse()
    print(v)
if(__name__=='__main__'):
    arr=[3,1,4,5,2]
    NGE(arr,len(arr))