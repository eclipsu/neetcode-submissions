import heapq
from collections import deque   
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        heap = [-ct for ct in count.values()]
        heapq.heapify(heap)

        queue = deque()
        
        time = 0

        while queue or heap:
            time += 1
            if heap:
                item = heapq.heappop(heap) + 1
                if item:
                    queue.append([item, time + n]) # _, idle time
            
            if queue and queue[0][1] <= time:
                heapq.heappush(heap,queue.popleft()[0])
        
        return time

