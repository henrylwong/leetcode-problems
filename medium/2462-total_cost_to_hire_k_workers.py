#!/usr/bin/env python3

import heapq

class Solution(object):
    MAX_COST = 10**5 + 1

    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """

        total_cost = 0

        first_heap_idx, last_heap_idx = candidates, len(costs) - candidates - 1
        if len(costs) < candidates * 2:
            last_heap_idx = candidates - 1
        first_heap, last_heap = costs[:candidates], costs[last_heap_idx + 1: len(costs)] 
        heapq.heapify(first_heap)
        heapq.heapify(last_heap)

        while k:
            # peek min of first_heap, peek min of last_heap
            first_heap_min = first_heap[0] if len(first_heap) else self.MAX_COST
            last_heap_min = last_heap[0] if len(last_heap) else self.MAX_COST

            # compare mins from both heaps and add smallest to total_cost
            # if equal, break tie using smallest index (which is in first heap)
            if first_heap_min == last_heap_min or first_heap_min < last_heap_min:
                total_cost += first_heap_min
                heapq.heappop(first_heap)
                if first_heap_idx <= last_heap_idx:
                    heapq.heappush(first_heap, costs[first_heap_idx])
                    first_heap_idx += 1
            else:
                total_cost += last_heap_min
                heapq.heappop(last_heap)
                if first_heap_idx <= last_heap_idx:
                    heapq.heappush(last_heap, costs[last_heap_idx])
                    last_heap_idx -= 1

            k -= 1
        
        return total_cost
    
if __name__ == "__main__":
    costs = [17,12,10,2,7,2,11,20,8]
    k = 3
    candidates = 4

    costs = [1, 2, 4, 1]
    k = 3
    candidates = 3

    # costs = [31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58]
    # k = 11
    # candidates = 2

    print("-" * 30)
    print("Executing soln...\n")

    soln = Solution()
    res = soln.totalCost(costs, k, candidates)

    print(res)