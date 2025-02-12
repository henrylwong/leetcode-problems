class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sums = dict() # max_num

        res = -1
        for num in nums:
            digit_sum = self._sumDigits(num)
            if digit_sum not in sums:
                sums[digit_sum] = num
            else:
                res = max(res, sums[digit_sum] + num)
                sums[digit_sum] = max(sums[digit_sum], num)

        return res

    def _sumDigits(self, num):
        res = 0
        while num > 0:
            res += num % 10
            num = num // 10
        return res