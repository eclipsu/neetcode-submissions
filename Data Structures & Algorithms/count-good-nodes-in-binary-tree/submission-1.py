# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def DFS(root, MAX):
            if not root:
                return 0
            
            res = 1 if root.val >= MAX else 0
            MAX = max(root.val, MAX)
            res += DFS(root.left, MAX)
            res += DFS(root.right, MAX)

            return res
        
        return DFS(root, root.val)