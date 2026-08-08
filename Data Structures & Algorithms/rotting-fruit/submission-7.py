from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        empty, fresh, rotton = 0, 1, 2
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        visited = set()
        fresh_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1

                
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        time = 0

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if (0 <= nc < cols) and (0 <= nr < rows) and (nr, nc) not in visited and grid[nr][nc] == fresh:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        fresh_count -= 1
            if queue:
                time += 1
        
        return time if fresh_count == 0 else -1