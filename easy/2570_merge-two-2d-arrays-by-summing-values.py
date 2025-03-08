class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        idx1, idx2 = 0, 0
        res = list()

        while idx1 < len(nums1) and idx2 < len(nums2):
            if idx1 < len(nums1) and nums1[idx1][0] <= nums2[idx2][0]:
                if len(res) and res[-1][0] == nums1[idx1][0]:
                    res[-1][1] += nums1[idx1][1]
                else:
                    res.append(nums1[idx1])
                idx1 += 1
            else:
                if len(res) and res[-1][0] == nums2[idx2][0]:
                    res[-1][1] += nums2[idx2][1]
                else:
                    res.append(nums2[idx2])
                idx2 += 1

        if idx2 >= len(nums2):
            while idx1 < len(nums1):
                if len(res) and res[-1][0] == nums1[idx1][0]:
                    res[-1][1] += nums1[idx1][1]
                else:
                    res.append(nums1[idx1])
                idx1 += 1
        else:
            while idx2 < len(nums2):
                if len(res) and res[-1][0] == nums2[idx2][0]:
                    res[-1][1] += nums2[idx2][1]
                else:
                    res.append(nums2[idx2])
                idx2 += 1

        return res