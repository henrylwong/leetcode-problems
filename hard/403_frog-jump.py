from typing import List

class Solution:
  def canCross(self, stones: List[int]) -> bool:
    dp = {i : set() for i in stones}
    dp[0].add(0)

    for stone in stones:
      if stone == stones[-1] and len(dp[stone]) > 0:
        return True

      for jump in dp[stone]:
        for delta in (-1, 0, 1):
          new_jump = jump + delta
          new_stone = stone + new_jump
          if new_jump > 0 and new_stone in dp:
            dp[new_stone].add(new_jump)

    return False
