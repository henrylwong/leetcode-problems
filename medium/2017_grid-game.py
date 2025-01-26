class Solution:
  def gridGame(self, grid: list[list[int]]) -> int:
    return self._minimizePoints(grid)
  
  def _minimizePoints(self, grid):
    top_sum = sum(grid[0]) - grid[0][0]
    bot_sum = 0

    min_points = top_sum
    for idx in range(1, len(grid[0])):
      top_sum -= grid[0][idx]
      bot_sum += grid[1][idx - 1]
      min_points = min(min_points, max(bot_sum, top_sum))

    return min_points