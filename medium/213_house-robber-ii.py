class Solution:
  def rob(self, nums: list[int]) -> int:
    N = len(nums)
    if N == 1:
      return nums[0]
    elif N == 2:
      return max(nums[0], nums[1])

    # Idx 0 -> N - 2
    memo = [0] * len(nums)
    memo[0], memo[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, N - 1):
      memo[i] = max(memo[i - 2] + nums[i], memo[i - 1])

    max1 = max(memo[-1], memo[-2])

    # Idx 1 -> N - 1
    memo = [0] * len(nums)
    memo[1], memo[2] = nums[1], max(nums[1], nums[2])

    for i in range(3, N):
      memo[i] = max(memo[i - 2] + nums[i], memo[i - 1]) 

    max2 = max(memo[-1], memo[-2])

    return max(max1, max2)