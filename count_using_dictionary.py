st=input()
d={}
for i in st:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)