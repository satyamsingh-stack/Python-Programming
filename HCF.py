def HCF(x,y):
    hcf=0
    if(x>y):
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if(x%i==0 and y%i==0):
            hcf=i
    return hcf
print(HCF(2,81))