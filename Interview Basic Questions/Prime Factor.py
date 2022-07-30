def primefactor(n):
    c=2
    while(n>1):
        if(n%c==0):
            print(c)
            n=n/c
        else:
            c=c+1
n=int(input())
primefactor(n)
