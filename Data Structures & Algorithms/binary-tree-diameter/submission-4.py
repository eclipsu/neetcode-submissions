# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def DFS(current):
            
            if not current:
                return 0
            
            left = DFS(current.left)
            right = DFS(current.right)

            self.result = max(self.result, left + right)
            return 1 + max(left, right)

        DFS(root)
        return self.result