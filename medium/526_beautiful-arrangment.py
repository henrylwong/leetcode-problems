class Solution:
    def countArrangement(self, n: int) -> int:
        self.res = 0
        self._countArrangement(1, {i for i in range(1, n+1)})
        return self.res
        
    def _countArrangement(self, idx, available_nums):
        if len(available_nums) == 0:
            self.res += 1
            return

        for num in [n for n in available_nums]:
            if num % idx and idx % num:
                continue
            
            available_nums.remove(num)
            self._countArrangement(idx + 1, available_nums)
            available_nums.add(num)
        return  