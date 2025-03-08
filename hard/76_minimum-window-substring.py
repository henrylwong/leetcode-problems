class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        occ_ref = dict()
        occ_s = dict()
        num_matches = 0
        res = None

        # Initialize occ of boh s and t
        for char in t:
            occ_ref[char] = occ_ref.get(char, 0) + 1
        for char in occ_ref:
            occ_s[char] = 0
        
        start_idx = 0
        for end_idx in range(len(s)):
            char = s[end_idx]
            if char in occ_ref:
                occ_s[char] += 1
            else:
                continue
            
            if not self._containsOcc(occ_ref, occ_s):
                continue
            
            while start_idx < end_idx:
                start_char = s[start_idx]
                if start_char not in occ_s:
                    start_idx += 1
                elif occ_s[start_char] > occ_ref[start_char]:
                    occ_s[start_char] -= 1
                    start_idx += 1
                else:
                    break

            if (res == None) or (end_idx - start_idx + 1 < len(res)):
                res = s[start_idx: end_idx + 1]
        if res == None:
            return ""
        return res
    
    def _containsOcc(self, occ_ref, occ_s):
        for k in occ_ref:
            if occ_ref[k] > occ_s[k]:
                return False
        return True