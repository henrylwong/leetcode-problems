from collections import deque
class Solution(object):

    PACIFIC = 1
    ATLANTIC = 2
    BOTH = 3

    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        flows = dict()
        flows[(0, len(heights[0]) - 1)] = self.BOTH
        flows[(len(heights) - 1, 0)] = self.BOTH
        pacific = self.get_shore(heights, self.PACIFIC)
        atlantic = self.get_shore(heights, self.ATLANTIC)

        ### PACIFIC TRAVERSAL ###
        queue = deque(pacific)
        while queue:
            m = queue.popleft()
            if m in flows:
                if flows[m] == self.ATLANTIC:
                    flows[m] = self.BOTH
            else:
                flows[m] = self.PACIFIC

            for neigh in self.get_neighbors(heights, m[0], m[1]):
                if neigh not in pacific and heights[neigh[0]][neigh[1]] >= heights[m[0]][m[1]]:
                    pacific.append(neigh)
                    queue.append(neigh)

        ### ATLANTIC TRAVERSAL ###
        queue = deque(atlantic)
        while queue:
            m = queue.popleft()
            if m in flows:
                if flows[m] == self.PACIFIC:
                    flows[m] = self.BOTH
            else:
                flows[m] = self.ATLANTIC

            for neigh in self.get_neighbors(heights, m[0], m[1]):
                if neigh not in atlantic and heights[neigh[0]][neigh[1]] >= heights[m[0]][m[1]]:
                    atlantic.append(neigh)
                    queue.append(neigh)

        res = list()
        for i in flows:
            if flows[i] == self.BOTH:
                res.append([i[0], i[1]])
        return res

    def get_shore(self, heights, ocean_type):
        '''Returns grid tiles adjacent to specified ocean'''
        res = list()
        len_row = len(heights[0])
        len_col = len(heights)
        if ocean_type == self.PACIFIC:
            for i in range(len_row):
                res.append((0, i))
            for j in range(1, len_col):
                res.append((j, 0))
        elif ocean_type == self.ATLANTIC:
            for i in range(0, len_row):
                res.append((len_col - 1, i))
            for j in range(0, len_col - 1):
                res.append((j, len_row - 1))
        return res


    def get_neighbors(self, heights, row, col):
        '''Returns valid neighbors to each grid tile'''
        res = list()

        if (row > 0):
            res.append((row-1, col))
        if (col > 0):
            res.append((row, col-1))
        if (row < len(heights) - 1):
            res.append((row+1, col))
        if (col < len(heights[0]) - 1):
            res.append((row, col+1))
        return res
