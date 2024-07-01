
class Node:
    def __init__(self, val):
        self.val=val
        self.next = None

class LinkList:
    def __init__(self):
        self.head=None
    
    # Function to insert a new node at the beginning
    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head =node
    def printList(self):
        head = self.head
        while head:
            print(head.val, end=" ")
            head = head.next
        print()
        # 1 2 3 4 5

    def reverse(self):
        prev = None
        current = self.head
        while current:
            currentNext = current.next
            current.next = prev
            prev =current
            current = currentNext
        self.head = prev




llist = LinkList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
llist.printList()
llist.reverse()
llist.printList()
