class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def DFS(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 1

            if (row, col) in visited:
                return 0
                        

            if grid[row][col] == 0:
                return 1
            
            visited.add((row, col))
            
            return (
                DFS(row + 1, col) +
                DFS(row - 1, col) +
                DFS(row, col + 1) +
                DFS(row, col - 1)
            )
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return DFS(row, col)