#!/usr/bin/env python3

from collections import deque
import math

class Solution:
  modulo = ((10 ** 9) + 7)

  def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    memo = dict()
    return self._recur(n, k, target, memo)

  def _recur(self, n, k, target, memo):
    if n == 1:
      if target <= k:
        num_ways = 1
      else:
        num_ways = 0
      memo[(1, k, target)] = num_ways 
      return num_ways
    
    num_ways = 0
    for i in range(1, min(target, k + 1)):
      if (n - 1, k, target - i) in memo:
        num_ways += memo[(n - 1, k, target - i)]
      else:
        num_ways += self._recur(n - 1, k, target - i, memo)

    num_ways %= self.modulo
    memo[(n, k, target)] = num_ways
    return num_ways

    '''BFS Method'''
    # visited = set([0])
    # queue = deque([0])
    # # queue = deque(range(1, k + 1))

    # num_dice = 0
    # num_ways = 0
    # while queue and num_dice < n:
    #   for _ in range(len(queue)):
    #     cur_sum = queue.popleft()
    #     for i in range(1, k + 1):
    #       new_sum = cur_sum + i
    #       if new_sum < target and new_sum not in visited:
    #           queue.append(new_sum)
    #           # visited.add(new_sum)
    #       elif new_sum == target:
    #           print(cur_sum, i)
    #           num_ways += 1
    #   # print(queue)
    #   # print(visited)
    #   num_dice += 1

    # return num_ways % ((10 ** 9) + 7)
        
if __name__ == "__main__":
  # n = 1
  # k = 6
  # target = 3

  # n = 2
  # k = 6
  # target = 7

  # n = 30
  # k = 30
  # target = 500

  n = 2
  k = 5
  target = 10

  soln = Solution()
  res = soln.numRollsToTarget(n, k, target)
  print(res)
