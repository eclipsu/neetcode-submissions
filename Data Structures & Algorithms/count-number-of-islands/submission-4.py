class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
         
        visited = set()
        ROW = len(grid)
        COL = len(grid[0])
        count = 0

        def explore(grid, row, col) -> bool:
            
            validRow = 0 <= row < ROW
            validCol = 0 <= col < COL

            if not (validCol and validRow):
                return False
            

            if grid[row][col] == "0":
                return False

            position = str(row) + '-' + str(col)
            if position in visited:
                return False
                      
            visited.add(position)

            explore(grid, row + 1, col)
            explore(grid, row - 1, col)
            explore(grid, row, col + 1)
            explore(grid, row, col - 1)
        
            return True
        
        for row in range(ROW):
            for col in range(COL):
                if explore(grid, row, col):
                    count += 1
        
        return count