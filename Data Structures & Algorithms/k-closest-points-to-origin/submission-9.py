import math
import heapq

class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.dist(pt, (0, 0)), pt) for pt in points]
        heapq.heapify(distances)

        result = []
        
        for _ in range(k):
            distance , points = heapq.heappop(distances) 
            result.append(points)
        
        return result