def GCD(a,b):
    if(b==0):
        return a
    else:
        return GCD(b,a%b)
a,b=54,24
print(GCD(a,b))



# def hcf(a,b):
#     if b==0:
#         return a
#     else:
#         return hcf(b, a%b)
# first = int(input('Enter first number: '))
# second = int(input('Enter second number: '))
# print('HCF or GCD of %d and %d is %d' %(first, second, hcf(first, second)))