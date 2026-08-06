from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))

        if not queue:
            return

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        distance = 0

        while queue:
            for _ in range(len(queue)): 
                row, col = queue.popleft()
                grid[row][col] = distance

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS
                            and (nr, nc) not in visited
                            and grid[nr][nc] != -1):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            distance += 1