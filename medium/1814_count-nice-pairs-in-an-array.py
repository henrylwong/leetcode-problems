#!/usr/bin/env python3

class Solution:
  modulo = (10 ** 9) + 7
  def _rev(num):
    return int(str(num)[::-1])

  def countNicePairs(self, nums: list[int]) -> int:
    diffs = dict()
    for i in range(len(nums)):
      diff = nums[i] - Solution._rev(nums[i])
      if diff not in diffs:
        diffs[diff] = 0
      diffs[diff] += 1
    
    res = 0
    for diff in diffs:
      n = diffs[diff]
      res += (n - 1) * n / 2
    return int(res) % self.modulo

if __name__ == "__main__":
  nums = [42, 11, 1, 97] # 2
  nums = [13, 10, 35, 24, 76] # 4

  soln = Solution()
  res = soln.countNicePairs(nums)
  print(res)