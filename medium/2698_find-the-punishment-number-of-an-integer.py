class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            square_i = i * i
            self.target = i
            if self._isPartitionable(square_i, []):
                res += square_i
        return res

    def _isPartitionable(self, square_i, nums):
        if square_i == 0:
            if sum(nums) == self.target:
                return True
            return False

        digit = 0
        base = 1
        while square_i > 0:
            digit = base * (square_i % 10) + digit
            square_i = square_i // 10
            base *= 10

            nums.append(digit)
            if self._isPartitionable(square_i, nums):
                return True
            nums.pop()
        
        return False