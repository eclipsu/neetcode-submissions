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
                    queue.append((row, col))
                if grid[row][col] == fresh:
                    fresh_count += 1
        time = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                
                    if (0 <= nr < rows) and (0 <= nc < cols) and (nr, nc) not in seen and grid[nr][nc] == fresh:
                        seen.add((nr, nc))
                        queue.append((nr, nc))
                        fresh_count -= 1
            if queue:
                time += 1
                

        return time if fresh_count == 0 else -1