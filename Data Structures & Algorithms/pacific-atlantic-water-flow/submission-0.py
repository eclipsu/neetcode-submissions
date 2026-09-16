class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs(row, col, ocean, previous):
            if (row, col) in ocean:
                return
            if not (0 <= row < rows and 0 <= col < cols):
                return
            if heights[row][col] < previous:
                return

            ocean.add((row, col))

            dfs(row + 1, col, ocean, heights[row][col])
            dfs(row - 1, col, ocean, heights[row][col])
            dfs(row, col + 1, ocean, heights[row][col])
            dfs(row, col - 1, ocean, heights[row][col])
            return

        ans = []
        rows = len(heights)
        cols = len(heights[0])

        pacific, atlantic = set(), set()

        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, cols - 1, atlantic, heights[row][cols - 1])

        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(rows - 1, col, atlantic, heights[rows - 1][col])

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    ans.append([row, col])

        return ans