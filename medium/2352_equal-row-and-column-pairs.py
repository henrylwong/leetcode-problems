#!/usr/bin/env python3

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        res = 0

        rows = dict()
        for idx in range(len(grid)):
            if tuple(grid[idx]) not in rows:
                rows[tuple(grid[idx])] = list()
            rows[tuple(grid[idx])].append(idx)

        for r_idx in range(len(grid)):
            col = list()
            for c_idx in range(len(grid)):
                col.append(grid[c_idx][r_idx])

            if tuple(col) in rows:
                res += len(rows[tuple(col)])
        
        return res
