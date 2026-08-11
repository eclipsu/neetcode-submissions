class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        seen = set()
        result = []

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0

        stack = [(0, 0)]

        while stack:
            row, col = stack.pop()

            if (row, col) in seen or not (0 <= row < rows and 0 <= col < cols):
                continue

            seen.add((row, col))
            result.append(matrix[row][col])

            dr, dc = directions[dir_idx]
            nr, nc = row + dr, col + dc

            if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) in seen:
                dir_idx = (dir_idx + 1) % 4
                dr, dc = directions[dir_idx]
                nr, nc = row + dr, col + dc

            stack.append((nr, nc))

        return result