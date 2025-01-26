#!/usr/bin/env python3

class Solution(object):
    # def rob(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     self.memo = dict()
    #     return self._rob(nums, 0)

    # def _rob(self, nums, idx):
    #     if idx >= len(nums):
    #         return 0
    #     elif idx in self.memo:
    #         return self.memo[idx]
    #     else:
    #         res = max(nums[idx] + self._rob(nums, idx + 2), self._rob(nums, idx + 1))
    #         self.memo[idx] = res
    #         return res
    # 

    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]

        memo = [0] * len(nums)
        memo[0], memo[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, N):
            memo[i] = max(memo[i - 2] + nums[i], memo[i - 1])
        
        return max(memo[-1], memo[-2])

if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    output = 12

    res = Solution().rob(nums)
    print(res)
    assert(res == output)