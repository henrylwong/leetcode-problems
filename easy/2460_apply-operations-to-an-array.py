class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res_idx = 0

        for idx in range(len(nums) - 1):
            cur_num = nums[idx]
            nxt_num = nums[idx + 1]
            
            if cur_num == nxt_num and cur_num != 0:
                res[res_idx] = cur_num * 2
                nums[idx + 1] = 0
                res_idx += 1
            elif cur_num != 0:
                res[res_idx] = cur_num
                res_idx += 1

        if nums[-1] != 0:
            res[res_idx] = nums[-1]
        
        return res