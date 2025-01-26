class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    memo = {1: cost[0], 2: cost[1]}
    n = len(cost)
    if n in memo: 
      return min(memo[n], memo[n-1])
    
    for i in range(3, n + 1):
      memo[i] = cost[i - 1] + min(memo[i - 2], memo[i - 1])
    
    return min(memo[n], memo[n - 1])