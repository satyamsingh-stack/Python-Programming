def convert24(st):
    if(st[:-2]=="AM" and st[:2]=="12"):
        return "00"+st[2:]
    elif(st[:-2]=="AM"):
        return st[:-2]
    elif(st[:-2]=="PM" and st[:2]=="12"):
        return st[:-2]
    else:
        return str(int(st[:2]) + 12) + st[2:-2]
st="00:00:00 AM"
print(convert24(st))