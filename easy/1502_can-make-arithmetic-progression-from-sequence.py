class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr = sorted(arr)
        delta = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != delta:
                return False

        return True