class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.res = list()
        self.wordDict = wordDict
        self._findWords(s, 0, list())
        return self.res

    def _findWords(self, s, start, words):
        for word in self.wordDict:
            end = start + len(word)
            if end <= len(s):
                if s[start: start + len(word)] == word:
                    words.append(word)
                    if end == len(s):
                        self.res.append(" ".join(words))
                    else:
                        self._findWords(s, end, words)
                    words.pop()
        return
            