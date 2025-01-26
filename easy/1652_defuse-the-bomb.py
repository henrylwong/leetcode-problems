#!/usr/bin/env python3

class Solution:
  def decrypt(self, code: list[int], k: int) -> list[int]:
    res = [0] * len(code)
    if k == 0:
      return res

    k_sum = 0
    for idx in range(abs(k)):
      k_sum += code[idx]

    idx = 0 
    while idx < len(code):
      circ_idx = (idx + abs(k)) % len(code)
      if k < 0:
        res[circ_idx] = k_sum
      k_sum += code[circ_idx] - code[idx]
      if k > 0:
        res[idx] = k_sum
      idx += 1
    return res

if __name__ == "__main__":
  cases = {
    ((5,7,1,4), 3): [12,10,16,13],
    ((2,4,9,3), -2): [12,5,6,13],
  }

  soln = Solution()
  for case in cases:
    print(f"Running case: {case}")
    res = soln.decrypt(*case)
    print(f"\tResult: {res}")
    if res == cases[case]:
      print(f"\t\033[92m\tStatus: PASS\033[0m")  
    else:
      print(f"\t\033[91m\tStatus: FAIL\033[0m")