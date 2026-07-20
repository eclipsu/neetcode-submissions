class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        seen = set()

        def dfs(rows, cols, index):
            if len(word) == index:
                return True

            if (rows < 0 or cols < 0 or rows >= ROWS or cols >= COLS or (rows, cols) in seen or board[rows][cols] != word[index]):
                return False
            
            seen.add((rows, cols))
            found = (
                dfs(rows + 1, cols, index + 1) or
                dfs(rows - 1, cols, index + 1) or
                dfs(rows, cols + 1, index + 1) or
                dfs(rows, cols - 1, index + 1)
            )
            seen.remove((rows, cols))
            return found
            

        
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        
        return False
