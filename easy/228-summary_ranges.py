class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if len(nums) <= 0:
            return []

        cur_range_start = nums[0]
        last_num = nums[0]
        res = list()

        for i in range(1, len(nums)):    
            cur_num = nums[i]
            if cur_num == last_num + 1:
                last_num = cur_num
            else:
                if cur_range_start == last_num:
                    res.append(str(cur_range_start))
                else:
                    res.append(str(cur_range_start) + "->" + str(last_num))
                cur_range_start = cur_num
                last_num = cur_range_start
            
        if nums[-1] == cur_range_start:
            res.append(str(cur_range_start))
        else:
            res.append(str(cur_range_start) + "->" + str(nums[-1]))
        
        return res


