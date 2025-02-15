import copy

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = list()
        self._restoreIPs(s, 0, list())
        return self.res
        
    def _createAddress(self, all_ints):
        assert(len(all_ints)) == 4
        return ".".join([str(i) for i in all_ints])
        
    def _restoreIPs(self, s, start, prefix):
        if len(prefix) >= 4 and start == len(s):
            self.res.append(self._createAddress(prefix))
            return 
        if len(prefix) >= 4 and start < len(s):
            return
        if start >= len(s) or len(prefix) > 4:
            return
        
        # Greedily take 0s because digits cannot have leading zeros
        if s[start] == '0':
            prefix.append(0)
            self._restoreIPs(s, start + 1, prefix)
            prefix.pop()
            return
        
        for idx in range(1, 4):
            octet = int(s[start: start + idx])
            if 0 <= octet <= 255:
                prefix.append(octet)
                self._restoreIPs(s, start + idx, prefix)
                prefix.pop()
        return