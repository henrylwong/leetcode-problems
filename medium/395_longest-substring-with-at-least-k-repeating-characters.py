from collections import Counter
import heapq

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        cnt = Counter(s)
        return self.validateSubstring(s, k, cnt)
        
    def validateSubstring(self, s, k, counter):
        heap = [(-(len(s)), 0, len(s) - 1, counter)]

        while heap:
            length, i, j, cnt = heapq.heappop(heap)

            invalid_chars = set()
            for char in cnt:
                if cnt[char] < k:
                    invalid_chars.add(char)

            if len(invalid_chars) == 0:
                return length * -1
            prev_idx = i
            new_cnt = Counter()
            for idx in range(i, j + 1):
                if s[idx] in invalid_chars:
                    new_length = idx - prev_idx
                    if len(new_cnt) > 0:
                        new_cnt_cpy = new_cnt
                        heapq.heappush(heap, (-new_length, prev_idx, idx - 1, new_cnt_cpy))
                        new_cnt = Counter()
                    prev_idx = idx + 1
                else:
                    print(s[idx])
                    new_cnt[s[idx]] += 1
                    print(new_cnt)
            if len(new_cnt) > 0:
                new_length = idx - prev_idx + 1
                heapq.heappush(heap, (-new_length, prev_idx, idx, new_cnt))

        return 0

