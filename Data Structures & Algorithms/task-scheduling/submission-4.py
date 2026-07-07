from collections import deque
from collections import Counter
import heapq

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
                print(heap)
                task = 1 + heapq.heappop(heap)
            
                if task != 0:
                    queue.append([task, time + n])
            
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        
        return time
                