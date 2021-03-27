class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, key):
        h = self.head
        if (h is None):
            new_node = Node(key)
            self.head = new_node
        else:
            while (h.next != None):
                h = h.next
            new_node = Node(key)
            h.next = new_node

    def sum_at_end(self):
        h = self.head
        if (h is None):
            print("Linkedlist is Empty")
        else:
            while (h.next != None):
                h = h.next
            h.data = h.data + 1

    def printlist(self):
        h = self.head
        while (h):
            print(h.data, end=" ")
            h = h.next
        print()

    def printlist1(self):
        h = self.head
        while (h):
            print(h.data, end="")
            h = h.next
        print()


if (__name__ == '__main__'):
    mylist = Linkedlist()
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    print("Intially Linkedlist is:", end=" ")
    mylist.printlist()
    mylist.sum_at_end()
    print("After addon end:", end="")
    mylist.printlist1()