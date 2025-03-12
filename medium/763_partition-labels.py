class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chr_hash = {}
        result = []

        for i in range(len(s)):
            chr_hash[s[i]] = i
        
        cur_end = 0
        cur_start = 0
        for i, c in enumerate(s):
            cur_end = max(chr_hash[c], cur_end)
            if i == cur_end:
                result.append(cur_end - cur_start + 1)
                cur_start = i + 1
        
        return result