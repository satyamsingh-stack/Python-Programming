import sys
class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
class StackLinkedList:
    def __init__(self):
        self.root = None
    def isEmpty(self):
        if (self.root is None):
            return True
        return False
    def push(self, key):
        node = Node(key)
        node.next = self.root
        self.root = node
        print("The element is pushed and top points to => ", self.root.data)
    def pop(self):
        deletedElement = -sys.maxsize - 1
        if (self.isEmpty()):
            print("Stack Underflow")
        else:
            deletedElement = self.root.data
            self.root = self.root.next
        return deletedElement
    def peek(self):
        topElement = -sys.maxsize - 1
        if (self.isEmpty()):
            print("Stack Underflow")
        else:
            topElement = self.root.data
        return topElement
if __name__ == '__main__':
    s = StackLinkedList()
    s.push(10)
    s.push(20)
    s.push(30)
    deletedElement = s.pop()
    print("Deleted Element: ", deletedElement)
    print("Top element is: ", s.peek())