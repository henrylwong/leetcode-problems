class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_neg = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    num_neg += len(grid[i]) - j
                    break

        return num_neg