#!/usr/bin/env python3

from collections import deque

class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """

        # cells preprocessing: list -> set for hashable elements
        cells = [tuple(cell) for cell in cells]

        # lo, mid, hi: crossing days
        lo = 0
        hi = len(cells) - 1
        last_valid_day = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            visited = set(cells[:mid])
            queue = deque(self._get_start_cells(visited, col))
            visited.update(queue)

            while queue:
                cell = queue.popleft()
                if cell[0] == row:
                    last_valid_day = mid
                    break

                for neighbor_cell in self._get_cardinal_neighbors(cell, row, col):
                    if neighbor_cell not in visited:
                        queue.append(neighbor_cell)
                        visited.add(neighbor_cell)
            
            if last_valid_day == mid:
                lo = mid + 1
            else:
                hi = mid - 1

        return last_valid_day

    def _get_start_cells(self, visited, col):
        start_cells = list()
        for c in range(1, col + 1):
            start_cell = (1, c)
            if start_cell not in visited:
                start_cells.append(start_cell)
        return start_cells

    def _get_cardinal_neighbors(self, cell, row, col):
        neighbor_cells = list()
        cell_row, cell_col = cell
        if cell_row > 1:
            neighbor_cells.append((cell_row - 1, cell_col))
        if cell_col > 1:
            neighbor_cells.append((cell_row, cell_col - 1))
        if cell_row < row:
            neighbor_cells.append((cell_row + 1, cell_col))
        if cell_col < col:
            neighbor_cells.append((cell_row, cell_col + 1))
        return neighbor_cells