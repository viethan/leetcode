# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return
        
        slow_runner = fast_runner = head
        
        while slow_runner and fast_runner and fast_runner.next:
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next
            
            if slow_runner == fast_runner:
                return True
        return False
