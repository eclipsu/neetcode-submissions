class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap) 

        print(heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if y > x:
                heapq.heappush(heap, -(y - x))
            elif x > y:
                heapq.heappush(heap, -(x - y))
        
        print(heap)
        return -heap[0] if len(heap) == 1 else 0
