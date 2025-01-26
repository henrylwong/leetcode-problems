class Solution:
  def beautifulSplits(self, nums: list[int]) -> int:
    if len(nums) < 3:
      return 0
    elif len(nums) == 3:
      if nums[0] == nums[1] or nums[2] == nums[3]:
        return 1

    num_splits = self.beautifulSplits(nums[:-1])
    
