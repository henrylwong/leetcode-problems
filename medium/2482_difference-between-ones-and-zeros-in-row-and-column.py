#!/usr/bin/env python3

import numpy as np

class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        res = list()
        onesRow = [0] * len(grid)
        onesCol = [0] * len(grid[0])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    onesRow[r] += 1
                    onesCol[c] += 1

        for r in range(len(grid)):
            res.append(list())
            for c in range(len(grid[0])):
                # res[r].append(onesRow[r] + onesCol[c] - (len(grid) - onesRow[r]) - (len(grid[0]) - onesCol[c]))
                res[r].append(2 * onesRow[r] - len(grid) + 2 * onesCol[c] - len(grid[0]))

        return res

if __name__ == "__main__":
    grid = [[0,1,1],[1,0,1],[0,0,1]]
    
    soln = Solution()
    res = soln.onesMinusZeros(grid)
    print(res)