# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next= None):
        self.val = val
        self.next = None
        

class LinkedList:
    def __init__(self, val):
        new_node = ListNode(val)
        self.head = new_node
        self.tail = new_node

        
    def append(self, val):
        new_node = ListNode(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.val)
        temp = temp.next    
            
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_head, bigger_head = ListNode(-1), ListNode(-1)
        less_prev, bigger_prev =less_head, bigger_head
        while head:
            if  head.val<x:
                less_prev.next = head
                less_prev =less_prev.next
            else:
                bigger_prev.next = head
                bigger_prev =bigger_prev.next
            head = head.next
        less_prev.next = bigger_prev.next = None
        less_prev.next = bigger_head.next
        return less_head


my_linked_listv1 = LinkedList(1)
my_linked_listv1.append(4)
my_linked_listv1.append(3)
my_linked_listv1.append(2)
my_linked_listv1.append(5)
my_linked_listv1.append(2)

ll = Solution().partition(my_linked_listv1.head, 3)

        
print_list(ll)
                

