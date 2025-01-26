#!/usr/bin/env python3

from collections import deque

class Solution:
  def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
    next_hops = [[i + 1] for i in range(n - 1)]
    next_hops.append([])
    dst = [i for i in range(n)]
    res = list()

    for query in queries:
      u, v = query
      next_hops[u].append(v) # assuming no duplicates

      is_terminated = False
      queue = deque([u])
      while queue and not is_terminated:
        node = queue.popleft()
        for next_hop in next_hops[node]:
          if dst[next_hop] > dst[node] + 1:
            dst[next_hop] = dst[node] + 1
            queue.append(next_hop)
          if next_hop == n - 1: 
            is_terminated = True
            break
      res.append(dst[n - 1]) 
       
    return res
  
if __name__ == "__main__":
  cases = {
    (5, ((2, 4), (0, 2), (0, 4))): (3, 2, 1),
    (4, ((0, 3), (0, 2))): (1, 1),
    (8, ((1, 5), (0, 2), (2, 6))): (4, 4, 3),
    (15, ((6, 11), (7, 11), (11, 14))): (10, 10, 8),
    (5, ((1, 3), (2, 4))): (3, 3)
  }

  soln = Solution()
  for case in cases:
    print(f"Running case: {case}")
    res = soln.shortestDistanceAfterQueries(*case)
    print(f"\tResult: {res}")
    if tuple(res) == cases[case]:
      print(f"\t\033[92m\tStatus: PASS\033[0m")
    else:
      print(f"\t\033[91m\tStatus: FAIL\033[0m")