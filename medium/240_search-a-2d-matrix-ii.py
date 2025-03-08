class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = len(matrix) - 1, 0

        num = matrix[x][y]
        visited = set()
        while num != target:
            if (x, y) in visited:
                return False
            visited.add((x, y))
            if num < target:
                y += 1
            else:
                x -= 1
            try:
                num = matrix[x][y]
            except IndexError:
                return False  

        return True