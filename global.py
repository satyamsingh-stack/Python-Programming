a=10
def something():
    global a
    a=15
    print("in fun",a)
something()
print("outside",a)