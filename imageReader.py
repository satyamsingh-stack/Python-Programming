f=open('MyImage.jpg','rb')

f1=open('Mypic.jpg','wb')
for i in f:
    f1.write(i)