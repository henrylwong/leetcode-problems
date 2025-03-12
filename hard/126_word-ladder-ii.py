from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        self.beginWord = beginWord
        self.endWord = endWord
        self.res = list()
        
        wordList.append(beginWord)
        word_set = {wordList[idx]: idx for idx in range(len(wordList))}
        alphabet = [chr(c) for c in range(ord('a'), ord('z') + 1)]
        word_graph = {word: list() for word in wordList}
        dist_to_end = {word: float('inf') for word in wordList}
        dist_to_end[endWord] = 0
        
        # Calculate distance heuristic
        seq_len = 1
        queue = deque([endWord])
        visited = set()
        while queue:
            do_terminate = False
            for _ in range(len(queue)):
                word = queue.popleft()
                if word in visited:
                    continue
                visited.add(word)
                for idx, char in ((idx, char) for idx in range(len(word)) for char in alphabet):
                    new_word = word[:idx] + char + word[idx + 1:]
                    if new_word in word_set and new_word not in visited: 
                        word_graph[new_word].append(word)
                        dist_to_end[new_word] = min(dist_to_end[new_word], seq_len)
                        if new_word == beginWord:
                            do_terminate = True
                        else:
                            queue.append(new_word)
            seq_len += 1
            if do_terminate:
                break

        # Run DFS w/ backtracking to capture all valid sequences
        self._dfs([len(wordList) - 1], word_graph, word_set, wordList, dist_to_end)

        return self.res

    def _dfs(self, seq, word_graph, word_set, word_list, dist_to_end):
        if len(seq) > dist_to_end[self.beginWord] + 1:
            return
        if seq[-1] == word_set[self.endWord]:
            self.res.append([word_list[word_idx] for word_idx in seq])
            return

        word = word_list[seq[-1]]
        for next_word in word_graph[word]:
            if dist_to_end[self.beginWord] != len(seq) + dist_to_end[next_word]:
                continue
            seq.append(word_set[next_word])
            self._dfs(seq, word_graph, word_set, word_list, dist_to_end)
            seq.pop()
        return