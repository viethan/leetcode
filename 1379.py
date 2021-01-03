# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is None and cloned is None:
            return None
        
        nodes = deque()
        nodes.append((original, cloned))
        while nodes:
            node_og, node_cp = nodes.popleft()
            
            if node_og is target:
                return node_cp
            if node_og.left:
                nodes.append((node_og.left, node_cp.left))
            if node_og.right:
                nodes.append((node_og.right, node_cp.right))
            
            
