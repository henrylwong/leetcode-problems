#!/usr/bin/env python3

class Solution:
  def maxCoins(self, piles: list[int]) -> int:
    piles.sort()
    my_idx = -2
    my_coins = 0
    for i in range(len(piles) // 3):
      my_coins += piles[my_idx]
      my_idx -= 2
    return my_coins
    


if __name__ == "__main__":
  piles = [2,4,1,2,7,8] # 9
  # piles = [2,4,5] # 4
  piles = [9,8,7,6,5,1,2,3,4] # 18

  soln = Solution()
  res = soln.maxCoins(piles)
  print(res)