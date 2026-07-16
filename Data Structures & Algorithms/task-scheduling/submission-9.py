from collections import Counter
from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-value for value in counts.values()]
        queue = deque()
        heapq.heapify(heap)

        time = 0
        while heap or queue:
            time += 1
            
            if heap:
                task = 1 + heapq.heappop(heap)
                if task != 0 :
                    queue.append((task, time + n))
                
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

        return time