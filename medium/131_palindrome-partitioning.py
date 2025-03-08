class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = list()
        self._partition(s, 0, list())
        return self.res
    
    def _partition(self, s, start_idx, words):
        if start_idx >= len(s):
            self.res.append([word for word in words])
            return

        cur_str = ""
        for idx in range(start_idx, len(s)):
            cur_str += s[idx]
            if self._isPalindrome(cur_str):
                words.append(cur_str)
                self._partition(s, idx + 1, words)
                words.pop()

    def _isPalindrome(self, t):
        if t == t[::-1]:
            return True
        return False
