class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        parents = [i for i in range(n + 1)]
        ranks = [1] * (n + 1)

        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])

            # path compression
            return parents[node]


        
        def union(node_a, node_b):
            parent_a = find(node_a)
            parent_b = find(node_b)

            if parent_a == parent_b:
                return False
            
            if ranks[parent_a] > ranks[parent_b]:
                parents[parent_b] = parents[parent_a]
                
            elif ranks[parent_a] < ranks[parent_b]:
                parents[parent_a] = parent_b

            else:
                parents[parent_b] = parent_a
                ranks[parent_a] += 1


            return True
            
        
        for node_a, node_b in edges:
            if not union(node_a, node_b):
                return [node_a, node_b]