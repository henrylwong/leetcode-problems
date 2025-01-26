class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """

        lo = 1
        hi = maxSum
        index_val = None
        curSum = None
        last_valid_val = list()

        while lo <= hi:
            index_val = (lo + hi) // 2
            curSum = index_val
            seqSum = self.seqSum(index_val - 1)
            
            if index_val <= n - index:
                curSum += seqSum + n - index - index_val
            else:
                curSum += seqSum - self.seqSum(index + index_val - n)
            if index_val <= index:
                curSum += seqSum + index - index_val + 1
            else:
                curSum += seqSum - self.seqSum(index_val - index - 1)
            
            if curSum < maxSum:
                lo = index_val + 1
                last_valid_val = index_val
            elif curSum > maxSum:
                hi = index_val - 1
            else:
                return index_val

        return last_valid_val

    def seqSum(self, n):
        return (n ** 2 + n) / 2