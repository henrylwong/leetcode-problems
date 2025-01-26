from collections import deque

class Solution:
  def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
    res = [[None] * len(isWater[0]) for _ in range(len(isWater))]
    queue = deque([])

    for i in range(len(isWater)):
      for j in range(len(isWater[0])):
        if isWater[i][j] == 1:
          queue.append((i, j))
          res[i][j] = 0    
        
    while queue:
      for _ in range(len(queue)):
        i, j = queue.popleft()
        for neigh_x, neigh_y in self._getNeighbors(isWater, i, j):
          if res[neigh_x][neigh_y] != None:
            continue
          
          res[neigh_x][neigh_y] = res[i][j] + 1
          queue.append((neigh_x, neigh_y))

    return res
          
  def _getNeighbors(self, grid, x, y):
    res = list()

    if x > 0:
      res.append((x - 1, y))
    if y > 0:
      res.append((x, y - 1))
    if x < len(grid) - 1:
      res.append((x + 1, y))
    if y < len(grid[0]) - 1:
      res.append((x, y + 1))

    return res

class Solution:
  def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)] # West, North, East, South
    res = [[None] * len(isWater[0]) for _ in range(len(isWater))]
    queue = deque([])

    for i in range(len(isWater)):
      for j in range(len(isWater[0])):
        if isWater[i][j] == 1:
          queue.append((i, j))
          res[i][j] = 0    
        
    while queue:
      for _ in range(len(queue)):
        i, j = queue.popleft()
        height = res[i][j]
        for dire in directions:
          neigh_x, neigh_y = i + dire[0], j + dire[1]
          if neigh_x < 0 or neigh_x >= len(isWater) or neigh_y < 0 or neigh_y >= len(isWater[0]):
            continue
          if res[neigh_x][neigh_y] != None:
            continue
          
          res[neigh_x][neigh_y] = height + 1
          queue.append((neigh_x, neigh_y))

    return res