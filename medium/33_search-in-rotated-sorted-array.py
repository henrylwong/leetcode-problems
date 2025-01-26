class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i, j = 0, len(nums) - 1

        while i <= j:
            mid = (i + j) // 2
            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[i]:
                if target > nums[mid]:
                    i = mid + 1
                elif target < nums[i]:
                    i = mid + 1
                else:
                    j = mid - 1
            elif nums[mid] <= nums[i]:
                if target < nums[mid]:
                    j = mid - 1
                elif target > nums[j]:
                    j = mid - 1
                else:
                    i = mid + 1

        return -1