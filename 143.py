# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        
        length, node = 0, head
        
        while node != None:
            length += 1
            node = node.next
        
        mid_node = head
        for i in range(ceil(length / 2) - 1):
            mid_node = mid_node.next
        
        prev_node, current_node = None, mid_node.next
        mid_node.next = None
        
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            
        first_node, mid_node = head, prev_node
        
        while mid_node != None:
            next_node = first_node.next
            first_node.next = mid_node
            mid_node = mid_node.next
            first_node.next.next = next_node
            first_node = first_node.next.next
            
        return head
