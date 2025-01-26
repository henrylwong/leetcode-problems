#!/usr/bin/env python

class Solution:
  def foreignDictionary(self, words: list[str]) -> str:
    # Construct graph from provided words
    graph = dict()
    for word in words:
      for char in word:
        if char not in graph:
          graph[char] = list()

    # Can only deduce ordering from adjacent words
    for idx in range(0, len(words) - 1):
      word1, word2 = words[idx], words[idx + 1]

      # Find first occurence of char mismatch
      char1, char2 = word1[0], word2[0]
      common_len = min(len(word1), len(word2))
      for c_idx in range(common_len):
        if c_idx < len(word1):
          char1 = word1[c_idx]
        if c_idx < len(word2):
          char2 = word2[c_idx]
        if char1 != char2:
          break

      # Ordering is not lexicographically valid if word2 is a strict prefix of word1
      if c_idx == common_len - 1 and char1 == char2:
        if len(word1) > len(word2):
          return ""

      # Add edge from char1 -> char2
      if char1 != char2:
        graph[char1].append(char2) 

    res = ""
    incoming = {char: 0 for char in graph}
    start_chars = list()
    # Run topo sort on graph; if graph is not a DAG, return ""
    for cur_char in graph:
      for next_char in graph[cur_char]:
        incoming[next_char] += 1
    for cur_char in incoming:
      if incoming[cur_char] == 0:
        start_chars.append(cur_char)

    while len(start_chars) > 0:
      cur_char = start_chars.pop()
      for next_char in graph[cur_char]:
        incoming[next_char] -= 1
        if incoming[next_char] == 0:
          start_chars.append(next_char)
      res += cur_char

    if len(res) == len(graph):
      return res
    return ""
  
if __name__ == "__main__":
  cases = {
    ("hrn","hrf","er","enn","rfnn"): "hernf",
    ("z","o"): "zo",
    ("baa", "abcd", "abca", "cab", "cad"): "bdac",
    ("wrtkj","wrt"): "",
    ("z", "z"): "z"
  }

  soln = Solution()
  for case in cases:
    print(f"Running case: {case}")
    res = soln.foreignDictionary(list(case))
    print(f"\tResult: {res}")
    if res == cases[case]:
        print(f"\t\033[92m\tStatus: PASS\033[0m")  
    else:
        print(f"\t\033[91m\tStatus: FAIL\033[0m") 
