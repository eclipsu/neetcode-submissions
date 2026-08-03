class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        seen = set()

        def dfs(row, col, match):
            if match == len(word):
                return True
            
            # handle out of bounds, already visited, or letter mismatch
            if (row >= ROWS or col >= COLS or col < 0 or row < 0 
                    or (row, col) in seen 
                    or board[row][col] != word[match]):
                return False
            
            seen.add((row, col))

            found = (dfs(row + 1, col, match + 1) or
                     dfs(row - 1, col, match + 1) or 
                     dfs(row, col + 1, match + 1) or
                     dfs(row, col - 1, match + 1)) 

            seen.remove((row, col))

            return found
        
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        
        return False