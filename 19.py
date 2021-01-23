# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        before = ListNode(-1)
        before.next = head
        
        
        fast_node = before
        for i in range(1, n + 2):
            fast_node = fast_node.next
            
        slow_node = before
        
        while fast_node != None:
            slow_node = slow_node.next
            fast_node = fast_node.next
            
        slow_node.next = slow_node.next.next
        return before.next
