class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        self.res = 0
        visited = {
            "right-diag": set(),
            "left-diag": set(),
            "row": set(),
            "col": set()
        }
        self._fillBoard(n, visited, 0)
        return self.res
    
    def _fillBoard(self, n, visited, row):
        if row >= n:
            self.res += 1
            return

        for col in range(0, n):
            right_diag = row - col
            left_diag = row + col
            # Check if a queen can potentially exist at (row, col) given above queens
            if right_diag in visited["right-diag"] or \
               left_diag in visited["left-diag"] or \
               row in visited["row"] or \
               col in visited["col"]:
               continue

            # Update visited with new queen
            self._updateVisited(True, visited, right_diag, left_diag, row, col)

            self._fillBoard(n, visited, row + 1)

            # Cleanup
            self._updateVisited(False, visited, right_diag, left_diag, row, col)

    def _updateVisited(self, addMode, visited, right_diag, left_diag, row, col):
        if addMode:
            visited["right-diag"].add(right_diag)
            visited["left-diag"].add(left_diag)
            visited["row"].add(row)
            visited["col"].add(col)
        else:
            visited["right-diag"].remove(right_diag)
            visited["left-diag"].remove(left_diag)
            visited["row"].remove(row)
            visited["col"].remove(col)
        return