# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists is None:
            return 
        
        dic = {}
        
        min, max = float('inf'), -float('inf')
        i = 0
        head = ListNode(-1)
        while i < len(lists):
            head.next = lists[i]
            node = head
            
            if node.next != None and node.next.val < min:
                min = node.next.val
                
            while node.next != None:
                if node.next.val not in dic:
                    dic[node.next.val] = []
                dic[node.next.val].append(node.next)
                node = node.next
                
            if node.val > max:
                max = node.val
                
            i += 1
            
        if min == float('inf') or max == -float('inf'):
            return
        
        curr = None
        for value in range(min, max + 1):
            if value in dic:
                for node in dic[value]:
                    if curr is None:
                        curr = node
                        newHead = curr
                    else:
                        curr.next = node
                        curr = curr.next
                        
        return newHead
