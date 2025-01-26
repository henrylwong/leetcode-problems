#!/usr/bin/env python3

class Solution:
  def findTargetSumWays(self, nums: list[int], target: int) -> int:
    # OPT(nums, T) = \Sum_{op \in OPS}(OPT(nums[:-1], T + op * nums[-1]))
    # Base case: OPT(nums, T) = 1 if len(nums) == 1 and (+/-)nums[0] == T; o/w 0

    self.memo = dict()
    self.nums = nums

    return self._findTargetSumWays(len(nums), target)

  def _findTargetSumWays(self, length, target):
    if (length, target) in self.memo:
      return self.memo[(length, target)]
 
    if length == 0:
      self.memo[(length, target)] = int(target == 0)
      return self.memo[(length, target)]

    num = self.nums[length - 1]
    self.memo[(length, target)] = self._findTargetSumWays(length - 1, target + num) + self._findTargetSumWays(length - 1, target - num)
    return self.memo[(length, target)]

if __name__ == "__main__":
  cases = {
    ((1,1,1,1,1), 3): 5,
    ((1,), 1): 1
  }

  soln = Solution()
  for case in cases:
    print(f"Running case: {case}")
    res = soln.findTargetSumWays(*case)
    print(f"\tResult: {res}")
    if res == cases[case]:
        print(f"\t\033[92m\tStatus: PASS\033[0m")  
    else:
        print(f"\t\033[91m\tStatus: FAIL\033[0m")