class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = list()
        self._getNums(n, k, 1, list())
        return self.res

    def _getNums(self, n, k, cur_idx, cur_nums):
        if len(cur_nums) >= k:
            self.res.append(tuple(cur_nums))
            return
        if cur_idx > n:
            return
        
        cur_nums.append(cur_idx)
        self._getNums(n, k, cur_idx + 1, cur_nums)
        cur_nums.pop()
        self._getNums(n, k, cur_idx + 1, cur_nums)

        return