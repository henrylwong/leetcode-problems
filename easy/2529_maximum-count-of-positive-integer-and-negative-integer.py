class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l_idx, r_idx = 0, len(nums) - 1

        while l_idx < r_idx:
            mid = l_idx + (r_idx - l_idx) // 2
            if nums[mid] > 0:
                r_idx = mid - 1
            else:
                l_idx = mid + 1
 
        r_idx = max(r_idx, 0)
        while l_idx >= 0 and nums[l_idx] >= 0:
            l_idx -= 1

        left_side = l_idx + 1

        right_side = len(nums) - r_idx - 1
        if nums[r_idx] > 0:
            right_side += 1
        return max(left_side, right_side)