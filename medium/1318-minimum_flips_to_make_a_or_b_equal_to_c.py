from math import log, floor
class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """

        orig_ab = a | b
        max_bits = int(max(log(orig_ab, 2), log(c, 2))) + 1
        num_bits_to_change = 0
        
        for i in range(max_bits):
            c_bit = (c >> i) & 0x1
            orig_ab_bit = (orig_ab >> i) & 0x1
            if orig_ab_bit != c_bit:
                if c_bit == 1:
                    num_bits_to_change += 1
                elif (a >> i & 0x1) and (b >> i & 0x1):
                    num_bits_to_change += 2
                else:
                    num_bits_to_change += 1

        return num_bits_to_change