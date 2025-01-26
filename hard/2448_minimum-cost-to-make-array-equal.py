class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        unique_nums = sorted(list(set(nums)))

        lo = 0
        hi = len(unique_nums) - 1
        res = None

        while lo <= hi:
            mid = (lo + hi) // 2
            
            cost_mid = self._cost_by_pivot(nums, cost, unique_nums[mid])
            if res:
                res = min(res, cost_mid)
            else:
                res = cost_mid

            if mid > 0:
                cost_lo = self._cost_by_pivot(nums, cost, unique_nums[mid - 1])
            else:
                lo += 1
                continue
            if mid < len(unique_nums) - 1:
                cost_hi = self._cost_by_pivot(nums, cost, unique_nums[mid + 1])
            else:
                hi -= 1
                continue
            
            if cost_lo < cost_mid and cost_mid < cost_hi:
                hi = mid - 1
            elif cost_lo > cost_mid and cost_mid > cost_hi:
                lo = mid + 1
            else:
                return res
    
        return res

    def _cost_by_pivot(self, nums, cost, pivot):
        cur_cost = 0
        for idx in range(len(nums)):
            if pivot != nums[idx]:
                cur_cost += abs(nums[idx] - pivot) * cost[idx]

        return cur_cost