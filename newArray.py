from array import *
val=array('i',[1,2,3,4,5])
newArray= array(val.typecode,(a for a in val))
for a in newArray:
    print(a)
print(id(newArray))
print(id(val))
