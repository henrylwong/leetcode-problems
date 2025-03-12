class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        res = 0
        num_alternating = 1
        prev_color = colors[0]
        for idx in range(1, len(colors) + k - 1):
            color = colors[idx % len(colors)]
            if color == prev_color:
                num_alternating = 1
            else:
                num_alternating += 1
            if num_alternating >= k:
                res += 1
            prev_color = color
            
        return res