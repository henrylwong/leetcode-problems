class Solution:
  def findAnagrams(self, s: str, p: str) -> list[int]:
    # Impossible to create anagram of p in s if len(s) < len(p)
    if len(p) > len(s):
      return []

    res = list()
    ord_a = ord('a')
    ref_hist = {i:0 for i in range(26)}
    for char in p:
      char_idx = ord(char) - ord_a
      ref_hist[char_idx] += 1

    # Get first window
    hist = {i:0 for i in range(26)}
    for idx in range(len(p)):
      char = s[idx] 
      char_idx = ord(char) - ord_a
      hist[char_idx] += 1

    if hist == ref_hist:
      res.append(0)

    # Slide window
    for idx in range(len(p), len(s)):
      del_char = s[idx - len(p)]
      del_char_idx = ord(del_char) - ord_a
      hist[del_char_idx] -= 1

      char = s[idx] 
      char_idx = ord(char) - ord_a
      hist[char_idx] += 1

      if hist == ref_hist:
        res.append(idx - len(p) + 1)

    return res