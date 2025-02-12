class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        summ = 0
        prev_num = 0 # lowest bound == 1
        for num in nums:
            if num > prev_num:
                summ += num
            else:
                summ = num
            
            res = max(res, summ)
            prev_num = num
        return res
