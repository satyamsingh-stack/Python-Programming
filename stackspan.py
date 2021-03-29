def Stackspan(arr,n):
    s=[]
    v=[]
    span=[]
    for i in range(0,n):
        while(len(s)!=0 and s[-1][0]<=arr[i]):
            s.pop()
        if(len(s)==0):
            v.append(-1)
        else:
            v.append(s[-1][1])
        s.append([arr[i],i])
    for i in range(n):
        span.append(i-v[i])
    print(span)
if(__name__=='__main__'):
    a=[100,80,60,70,60,75,85]
    s=Stackspan(a,len(a))