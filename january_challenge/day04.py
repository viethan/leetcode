# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        head.next = l1
        
        node1, node2 = head, l2
        while node2 != None:
            if node1.next != None:
                if node1.next.val >= node2.val:
                    nexto = node1.next
                    node1.next = node2
                    node2 = node2.next
                    node1.next.next = nexto
                else:
                    node1 = node1.next
            else:
                node1.next = node2
                break
                
        return head.next
