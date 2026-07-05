# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def BFS(root):
            if not root:
                return []

            result = []
            q = deque([root])

            while q:
                size = len(q)
                res = []

                for _ in range(size):
                    current = q.popleft()
                    res.append(current.val)             

                    if current.left:
                        q.append(current.left)
                    
                    if current.right:
                        q.append(current.right)
                    
                result.append(res)
                
            print(result)
            return result
        
        return BFS(root)


        