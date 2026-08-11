class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        seen = set()

        area = 0
        def dfs(row, col):
            if (
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                (row, col) in seen or
                grid[row][col] == 0
            ):
                return 0


            seen.add((row, col))

            return (
                1
                + dfs(row + 1, col)
                + dfs(row - 1, col)
                + dfs(row, col + 1)
                + dfs(row, col - 1)
            )

        for row in range(rows):
            for col in range(cols):
                area = max(area, dfs(row, col))
        
        return area
