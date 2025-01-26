#!/usr/bin/env python3

class Solution:
  def makeEqual(self, words: list[str]) -> bool:
    char_counts = dict()
    for word in words:
      for char in word:
        if char not in char_counts:
          char_counts[char] = 0
        char_counts[char] += 1

    for count in char_counts.values():
      if count % len(words) != 0:
        return False
    return True

if __name__ == "__main__":
  words = ["abc","aabc","bc"]
  out = True

  words = ["ab","a"]
  out = False

  soln = Solution()
  res = soln.makeEqual(words)
  print(res)
  assert(res == out)     