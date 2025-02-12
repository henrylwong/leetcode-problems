from collections import deque

class Solution:
  def findMaxFish(self, grid: List[List[int]]) -> int:
    queue = deque([])
    visited = set()
    max_sum = 0

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] > 0 and (i, j) not in visited:
          queue.append((i, j))
          visited.add((i, j))
          sum = 0 
          while queue:
            x, y = queue.popleft()
            sum += grid[x][y]
            for delta_x, delta_y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
              new_x, new_y = x + delta_x, y + delta_y
              if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and (new_x, new_y) not in visited and grid[new_x][new_y] > 0:
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))

          max_sum = max(max_sum, sum)
    
    return max_sum