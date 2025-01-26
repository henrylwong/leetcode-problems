#!/usr/bin/env python3

class Solution(object):
  def findRelativeRanks(self, score):
    """
    :type score: List[int]
    :rtype: List[str]
    """
    ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    if len(score) > 3:
      ranks = ranks + [str(x) for x in range(4, len(score) + 1)]
    else:
      ranks = ranks[:len(score)]

    res = [""] * len(score)

    sorted_idxs = sorted(range(len(score)), key=lambda x: score[x], reverse=True)

    i = 0
    for idx in sorted_idxs:
      res[idx] = ranks[i]
      i += 1

    return res

if __name__ == "__main__":
  score = [10,3,8,9,4]
  
  soln = Solution()
  print(soln.findRelativeRanks(score))