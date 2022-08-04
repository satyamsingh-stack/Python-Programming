CHAR=256
def anagram(st1,st2):
    hash=[0]*CHAR
    if(len(st1)!=len(st2)):
        return False
    for i in range(len(st1)):
        hash[ord(st1[i])-ord('a')]+=1
        hash[ord(st2[i])-ord('a')]-=1
    for i in range(1,CHAR):
        if(hash[i]!=0):
            return False
    return True
st1=input()
st2=input()
print(anagram(st1,st2))
