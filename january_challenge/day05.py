# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next, node = head, dummy
        while node.next != None:
            if node.next.next and (node.next.val == node.next.next.val):
                kill = node.next.val
                while node.next and (node.next.val == kill):
                    node.next = node.next.next
            else:
                node = node.next
        return dummy.next
