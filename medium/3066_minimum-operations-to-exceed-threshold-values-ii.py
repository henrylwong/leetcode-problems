import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        res = 0
        while nums:
            if nums[0] >= k:
                return res
            x = heapq.heappop(nums)
            y = nums[0]
            y = heapq.heappushpop(nums, min(x, y) * 2 + max(x, y))

            res += 1
    
        return -1