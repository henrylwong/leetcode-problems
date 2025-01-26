class Solution:
    def countSubstrings(self, s: str) -> int:
      N = len(s)
      memo = dict()
      res = 0

      for length in range(1, N + 1):
        for i in range(N - length + 1):
          j = i + length - 1
          if length == 1:
            memo[(i, j)] = True
          elif length == 2:
            memo[(i, j)] = (s[i] == s[j])
          else:
            memo[(i, j)] = (s[i] == s[j]) and memo.get((i + 1, j - 1), False)

          if memo[(i, j)]:
              res += 1

      return res
    
    # Expanding Around Center Technique
    def countSubstrings(self, s: str) -> int:
      # Using Expanding Around Center Technique
      N = len(s)
      res = 0

      for idx in range(N):
        res += self._expandAroundCenter(s, idx, idx) + self._expandAroundCenter(s, idx, idx + 1)

      return res    

    def _expandAroundCenter(self, s, i, j):
      num_matches = 0
      while i >= 0 and j < len(s) and s[i] == s[j]:
        num_matches += 1
        i -= 1
        j += 1
      return num_matches
