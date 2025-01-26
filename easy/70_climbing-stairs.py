class Solution:
    def climbStairs(self, n: int) -> int:
        # OPT(n) = OPT(n - 1) + OPT(n - 2)
        # Base case: OPT(1) = 1; OPT(2) = 2
        
        memo = {1: 1, 2: 2}
        if n in memo:
            return memo[n]
        
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        
        return memo[n]