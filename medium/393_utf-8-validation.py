class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        idx = 0
        while idx < len(data):
            if (data[idx] >> 7) & 0x1 == 0: # 1-byte
                idx += 1
            else: # n-byte
                is_valid, offset = self._parseNbyte(data, idx)
                if not is_valid:
                    return False
                idx += offset
        return True

    def _parseNbyte(self, data, idx):
        n_val = 0
        num = data[idx]
        for i in range(7, 3, -1):
            if (num >> i) & 0b1 == 1:
                n_val += 1
            else:
                break
        
        if n_val == 1:
            return False, 0
        if (num >> (7 - n_val)) & 0b1 == 1:
            return False, 0
        
        n = idx + 1
        while n < idx + n_val:
            if n >= len(data):
                return False, 0
            num = data[n]
            if (num >> 6) & 0b11 != 0b10:
                return False, 0 
            n += 1
            
        return True, n_val