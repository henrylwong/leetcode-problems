class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        return self._isAdditiveNumber(num, 0, list())
        
    def _isAdditiveNumber(self, num, start_idx, sequence):
        if start_idx >= len(num):
            if len(sequence) >= 3:
                return True
            return False

        if num[start_idx] == '0':
            if not self._isAdditive(sequence, 0):
                return False
            
            sequence.append(0)
            if self._isAdditiveNumber(num, start_idx + 1, sequence):
                return True
            sequence.pop()
            return False

        cur_str = ""
        for idx in range(start_idx, len(num)):
            cur_str += num[idx]
            cur_num = int(cur_str)
            
            if not self._isAdditive(sequence, cur_num):
                continue
            
            sequence.append(cur_num)
            if self._isAdditiveNumber(num, idx + 1, sequence):
                return True
            sequence.pop()
        return False
    
    def _isAdditive(self, sequence, candidate_num):
        if len(sequence) < 2:
            return True
        if candidate_num == sequence[-2] + sequence[-1]:
            return True
        return False