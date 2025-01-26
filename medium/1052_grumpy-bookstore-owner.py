#!/usr/bin/env python3

class Solution(object):
  def maxSatisfied(self, customers, grumpy, minutes):
    """
    :type customers: List[int]
    :type grumpy: List[int]
    :type minutes: int
    :rtype: int
    """
    baseline_customers_satisfied = 0

    # Baseline
    for i in range(len(customers)):
      baseline_customers_satisfied += customers[i] * (1 - grumpy[i])
    
    # Init sliding window
    customers_satisfied = baseline_customers_satisfied
    for i in range(minutes):
      if grumpy[i]:
        customers_satisfied += customers[i]
    max_customers_satisfied = max(baseline_customers_satisfied, customers_satisfied)

    # Run sliding window
    l_idx, r_idx = 0, minutes
    while r_idx < len(customers):
      if grumpy[l_idx]:
        customers_satisfied -= customers[l_idx]
      if grumpy[r_idx]:
        customers_satisfied += customers[r_idx]
      
      max_customers_satisfied = max(max_customers_satisfied, customers_satisfied)
      l_idx += 1
      r_idx += 1

    return max_customers_satisfied
       
if __name__ == "__main__":
  customers = [1, 0, 1, 2, 1, 1, 7, 5]
  grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
  minutes = 3

  soln = Solution()
  print(soln.maxSatisfied(customers, grumpy, minutes))