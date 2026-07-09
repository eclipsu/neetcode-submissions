class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        seen = set() # existing path so far

        def dfs(row, col, index):
            
            # dfs isn't called again, but when it does, index = no of matched letters

            if index == len(word):
                return True

            # conditions
            # the row and col are out of bounds
            # current row and col are in path
            # the new letter in board isn't in the board

            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in seen or board[row][col] != word[index]):
                return False
            
            seen.add((row, col))
            
            found = (  dfs(row + 1, col, index + 1)
                    or dfs(row, col + 1, index + 1)
                    or dfs(row - 1, col, index + 1)
                    or dfs(row, col - 1, index + 1))
            seen.remove((row, col))

            return found
        
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        
        return False
