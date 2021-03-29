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
    def sortList(self):
        current = self.head
        index = None
        if (self.head == None):
            return
        else:
            while (current != None):
                index = current.next
                while (index != None):
                    if (current.data > index.data):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next
    def printlist(self):
        h=self.head
        while(h):
            print(h.data,end=" ")
            h=h.next
        print()
if(__name__=='__main__'):
    mylist=Linkedlist()
    mylist.appending(2)
    mylist.appending(9)
    mylist.appending(1)
    mylist.appending(0)
    mylist.appending(3)
    print("After appending Linkedlist is:",end=" ")
    mylist.printlist()
    mylist.sortList()
    print("After Sorting Linkedlist is:",end=" ")
    mylist.printlist()