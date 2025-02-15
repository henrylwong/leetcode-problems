class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # Greedily choose the highest digit possible for each idx and and return the first valid sequence
        seq = [0] * (2 * n - 1)
        self._constructSequence(seq, 0, set(range(1, n + 1)))
        return self.res

    def _constructSequence(self, seq, start_idx, nums_avail):
        '''
        :param seq: potentially incomplete sequence
        :param start_idx: idx to fill in given sequence
        :param nums_avail: set of numbers available to insert
        '''
        if start_idx == len(seq):
            if len(nums_avail) == 0:
                self.res = seq
                return True
            return False

        if seq[start_idx] != 0:
            return self._constructSequence(seq, start_idx + 1, nums_avail)

        for num in sorted(nums_avail, reverse=True):
            # Set num
            if num != 1:
                if start_idx + num >= len(seq) or seq[start_idx + num] != 0: # if other occurence is out of bounds or idx already occupied
                    continue
                seq[start_idx + num] = num
            seq[start_idx] = num
            nums_avail.remove(num)

            is_valid = self._constructSequence(seq, start_idx + 1, nums_avail)
            if is_valid:
                return True
            
            # Unset num
            seq[start_idx] = 0
            if num != 1: 
                seq[start_idx + num] = 0
            nums_avail.add(num)

        return False
