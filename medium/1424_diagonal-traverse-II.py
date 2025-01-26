#!/usr/bin/env python3

class Solution:
  def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
    groups = list()
    for r in range(len(nums)):
      for c in range(len(nums[r])):
        groups.append((r + c, -r, nums[r][c]))
    groups.sort()
    return [group[2] for group in groups]

if __name__ == "__main__":
  # nums = [[1,2,3],[4,5,6], [7, 8, 9]]
  # out = [1,4,2,7,5,3,8,6,9]

  # nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
  # out = [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

  nums = [[6],[8],[6,1,6,16]]
  out = [6,8,6,1,6,16]

  soln = Solution()
  res = soln.findDiagonalOrder(nums)
  print(res)
  assert(res == out)