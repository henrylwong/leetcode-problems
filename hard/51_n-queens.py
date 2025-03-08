class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = list()
        visited = {
            "right-diag": set(),
            "left-diag": set(),
            "row": set(),
            "col": set()
        }
        self._fillBoard(n, visited, list())
        return self.res
    
    def _fillBoard(self, n, visited, idxs):
        row = len(idxs)

        if row >= n:
            board_repr = self._generateRepr(n, idxs)
            self.res.append(board_repr)
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
            self._updateVisited(True, visited, idxs, right_diag, left_diag, row, col)

            self._fillBoard(n, visited, idxs)

            # Cleanup
            self._updateVisited(False, visited, idxs, right_diag, left_diag, row, col)

    def _generateRepr(self, n, idxs):
        assert(len(idxs) == n)
        board_repr = list()
        for col in idxs:
            row_repr = '.' * col + 'Q' + '.' * (n - col - 1)
            board_repr.append(row_repr)
        return board_repr

    def _updateVisited(self, addMode, visited, idxs, right_diag, left_diag, row, col):
        if addMode:
            visited["right-diag"].add(right_diag)
            visited["left-diag"].add(left_diag)
            visited["row"].add(row)
            visited["col"].add(col)
            idxs.append(col)
        else:
            visited["right-diag"].remove(right_diag)
            visited["left-diag"].remove(left_diag)
            visited["row"].remove(row)
            visited["col"].remove(col)
            idxs.pop()
        return