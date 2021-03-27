class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def appending(self,key):
        h=self.head
        if(h is None):
            new_node=Node(key)
            self.head=new_node
        else:
            while(h.next!=None):
                h=h.next
            new_node=Node(key)
            h.next=new_node
    def getcount(self):
        h=self.head
        count=0
        while(h):
            h=h.next
            count+=1
        print(count)
    def printlist(self):
        h=self.head
        while(h):
            print(h.data,end=" ")
            h=h.next
        print()
if(__name__=='__main__'):
    mylist=Linkedlist()
    mylist.appending(1)
    mylist.appending(2)
    mylist.appending(3)
    mylist.appending(4)
    print("After appending Linkedlist is:",end=" ")
    mylist.printlist()
    print("Total number node is:",end=" ")
    mylist.getcount()