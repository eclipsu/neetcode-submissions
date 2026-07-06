# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        def bfs(node):
            if not node:
                return "N,"
            
            result = ""
            queue = collections.deque([node])
            
            while queue:
                current = queue.popleft()
                
                if current:
                    result += str(current.val) + ","
                    queue.append(current.left)
                    queue.append(current.right)
                else:
                    result += "N,"
            return result

        return bfs(root)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        values.pop()

        if values[0] == "N":
            return None

        root = TreeNode(int(values[0]))
        queue = collections.deque([root])

        i = 1

        while queue:
            node = queue.popleft()

            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            
            i += 1

            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i+= 1
        
        return root




