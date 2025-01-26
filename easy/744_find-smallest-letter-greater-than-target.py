class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        smallest_char = None
        lo = 0
        hi = len(letters) - 1
 
        while lo <= hi:
            mi = (lo + hi) // 2
            if letters[mi] > target:
                smallest_char = letters[mi]
                hi = mi - 1
            elif letters[mi] <= target:
                lo = mi + 1
        
        return smallest_char if smallest_char != None else letters[0]
            