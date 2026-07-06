# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, left_boundry, right_boundry):
            if not root:
                return True
            
            if not (left_boundry < root.val and root.val < right_boundry):
                return False
            
            return (valid(root.left, left_boundry, root.val) and valid(root.right, root.val, right_boundry))
        
        return valid(root, float("-inf"), float("inf"))
