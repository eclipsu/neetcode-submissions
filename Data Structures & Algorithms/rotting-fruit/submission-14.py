from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        empty, fresh, rotton = 0, 1, 2
        rows, cols = len(grid), len(grid[0])

        fresh_count = 0
        seen = set()
        queue = deque() 

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == rotton:
                    queue.append((row, col, 0))
                if grid[row][col] == fresh:
                    fresh_count += 1
        max_time = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            for _ in range(len(queue)):
                row, col, time = queue.popleft()
                max_time = max(time, max_time)

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                
                    if (0 <= nr < rows) and (0 <= nc < cols) and (nr, nc) not in seen and grid[nr][nc] == fresh:
                        seen.add((nr, nc))
                        queue.append((nr, nc, time + 1))
                        fresh_count -= 1

        return max_time if fresh_count == 0 else -1