#!/usr/bin/env python3

class Solution:
  def resultsArray(self, nums: list[int], k: int) -> list[int]:
    res = list()
    asc_cnt = 0
    prev_num = 0

    idx = 0
    while idx < len(nums):
      next_num = nums[idx]
      if next_num == prev_num + 1:
        asc_cnt += 1
      else:
        asc_cnt = 1

      prev_num = next_num
      idx += 1

      if idx < k:
        continue

      if asc_cnt >= k:
        res.append(next_num)
      else:
        res.append(-1)

    return res
      
if __name__ == "__main__":
  cases = {
    ((1,2,3,4,3,2,5), 3): [3,4,-1,-1,-1],
    ((2,2,2,2,2), 4): [-1, -1],
    ((3,2,3,2,3,2), 2): [-1,3,-1,3,-1],
    ((1,3,4),2):[-1,4]
  }

  soln = Solution()
  for case in cases:
    print(f"Running case: {case}")
    res = soln.resultsArray(*case)
    print(f"\tResult: {res}")
    if res == cases[case]:
      print(f"\t\033[92m\tStatus: PASS\033[0m")  
    else:
      print(f"\t\033[91m\tStatus: FAIL\033[0m")