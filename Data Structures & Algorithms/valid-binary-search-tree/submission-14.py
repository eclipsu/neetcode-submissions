# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return []
            return dfs(root.left) + [root.val] + dfs(root.right)
        
        tree = dfs(root)
        for i in range(len(tree) - 1):
            if tree[i] >= tree[i + 1]:
                return False

        return True