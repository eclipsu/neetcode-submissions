import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-count for count in counts.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0
        
        while heap or queue:
            time += 1
            if heap:
                task = heapq.heappop(heap) + 1
                if task < 0:
                    queue.append([task, time + n])
            
            if queue and queue[0][1] == time:
                task, _ = queue.popleft()
                heapq.heappush(heap, task)
        
        return time