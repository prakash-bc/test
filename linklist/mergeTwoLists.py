# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # dummy ,tail = Node(0),Node(0)
        # while list1 and list2:
        #     print(list1.val, list2.val)
        #     if list1.val< list2.val:
        #         tail.next =list1
        #         list1 = list1.next
        #     else: 
        #         tail.next =list2
        #         list2 = list2.next
        #     tail = tail.next
        # tail.next = list1 or list2
        # # print(d.val, d.next.val,  d.next.next.val, d.next.next.next.val)
        # # print(tail.val, tail.next.val)
        # print("DDD====")
        dummy , tail = Node(0),Node(0)
        while list1 and list2:
            if list1.val< list2.val:
                tail.next = list1
                list1= list1.next
            else:
                tail.next = list2
                list2= list2.next
            tail = tail.next
        tail.next = list1 or list1
        head = tail
        while head:
            print(head.val, end=" ")
            head = head.next
        print()

llist1 = LinkList()
llist1.push(1)
llist1.push(2)
llist1.push(4)


llist2 = LinkList()
llist2.push(1)
llist2.push(3)
llist2.push(4)

Solution().mergeTwoLists(llist1.head, llist2.head)

# # https://www.javatpoint.com/indexing-in-dbms
# # which alog indexs uses
# # primary index vs secondary index
# # sharding
# # cap theorem
# when to use monolithic kernel
# # https://www.nitendratech.com/database/cap-theorem/
# what is scalable system means


# when to use buffered and unuffered channel

# how slice grown internally