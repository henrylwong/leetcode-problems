#!/usr/bin/env python3

class Solution:
  def findErrorNums(self, nums: list[int]) -> list[int]:
    zeros = set()
    for i in range(1, len(nums) + 1):
      zeros.add(i)
    ones = set()
    two = None

    for num in nums:
      if num in zeros:
        zeros.remove(num)
        ones.add(num)
      elif num in ones:
        two = num
    
    return [two, zeros.pop()]
  
if __name__ == "__main__":
  nums = [1,2,2,4]
  soln = Solution()
  print(soln.findErrorNums(nums))
