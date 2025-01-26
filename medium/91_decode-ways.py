#!/usr/bin/env python3

class Solution:
  def numDecodings(self, s: str) -> int:
    # OPT(N) = \Sum_{c \in valid mappings} OPT(N - len(c))
    # Base case: OPT(N) = 1 if N == 0; 0 if no valid mappings
    memo = [0] * (len(s) + 1)
    memo[0] = 1

    for idx in range(len(s)):
      cnt = 0
      if s[idx] != "0":
        cnt += memo[idx]
      if idx - 1 >= 0 and ((s[idx - 1] == "1") or (s[idx - 1] == "2" and int(s[idx]) <= 6)):
        cnt += memo[idx - 1]
      memo[idx + 1] = cnt

    return memo[len(s)]

if __name__ == "__main__":
  cases = {
     "12": 2,
     "226": 3,
     "06": 0,
     "27": 1,
     "11106": 2,
     "2101": 1,
     "2611055971756562": 4
  }

  soln = Solution()
  for case in cases:
    print(f"Running case: {case}")
    res = soln.numDecodings(case)
    print(f"\tResult: {res}")
    if res == cases[case]:
        print(f"\t\033[92m\tStatus: PASS\033[0m")  
    else:
        print(f"\t\033[91m\tStatus: FAIL\033[0m")