from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, minute it rotted)
                elif grid[r][c] == 1:
                    fresh_count += 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        max_time = 0

        while queue:
            row, col, t = queue.popleft()
            max_time = max(max_time, t)
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2          # mark rotten in place (no separate `seen` set needed)
                    fresh_count -= 1
                    queue.append((nr, nc, t + 1))

        return max_time if fresh_count == 0 else -1