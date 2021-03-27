class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertionatbeginning(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def insertionatend(self, key):
        h = self.head
        if (h is None):
            new_node = Node(key)
            self.head = new_node
        else:
            while (h.next != None):
                h = h.next
            new_node = Node(key)
            h.next = new_node

    def insertionafterward(self, after, key):
        h = self.head
        if (h is None):
            print("List is empty and can not not inserted")
            # return
        else:
            while (h.data != after):
                h = h.next
                if (h is None):
                    print("Can not be inserted")
                    # return
            new_node = Node(key)
            new_node.next = h.next
            h.next = new_node

    def deletioniteams(self,key):
        h = self.head
        prev = None
        if(h is None):
            print("The List is empty, the node can not be deleted")
            return
        if(h.data == key):
            self.head = h.next
        while(h is not None and h.data != key):
            prev = h
            h = h.next
        if(h is None):
            print("The key is not present in the List")
        prev.next = h.next
    def printlist(self):
        h = self.head
        while (h):
            print(h.data, end=" ")
            h = h.next
        print()

if (__name__ == '__main__'):
    myList = LinkedList()

    myList.insertionatbeginning(1)
    print("Intially LinkedList is:", end=" ")
    myList.printlist()

    myList.insertionatbeginning(0)
    print("After Insertion at beginning:", end=" ")
    myList.printlist()

    myList.insertionatend(2)
    print("After insertion at end:", end=" ")
    myList.printlist()

    myList.insertionafterward(1,1.5)
    print("After insertion in between:", end=" ")
    myList.printlist()

    myList.deletioniteams(1)
    print("After delete:", end=" ")
    myList.printlist()