# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i, j = 1, n
        
        while i <= j:
            mid = (i + j) // 2
            if isBadVersion(mid):
                if mid == 1 or not isBadVersion(mid - 1):
                    return mid
                j = mid - 1
            else:
                i = mid + 1
        
        return -1