from collections import deque

class Solution:
  def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    directions = ((0, -1), (-1, 0), (0, 1), (1, 0))
    res = [[None] * len(mat[0]) for _ in range(len(mat))]
    queue = deque([])

    for i in range(len(mat)):
      for j in range(len(mat[0])):
        if mat[i][j] == 0:
          queue.append((i, j))
          res[i][j] = 0
        
    while queue:
      for _ in range(len(queue)):
        i, j = queue.popleft()
        height = res[i][j]
        for dire in directions:
          neigh_x, neigh_y = i + dire[0], j + dire[1]
          if neigh_x < 0 or neigh_x >= len(mat) or neigh_y < 0 or neigh_y >= len(mat[0]):
            continue
          if res[neigh_x][neigh_y] != None:
            continue
          
          res[neigh_x][neigh_y] = height + 1
          queue.append((neigh_x, neigh_y))

    return res