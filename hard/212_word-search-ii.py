class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.res = list()
        self.words = words

        trie = self._computeTrie(words)
        self._dfs(board, set(), None, trie)
        return self.res

    def _dfs(self, board, visited, cur_idx, cur_trie):
        if '$' in cur_trie:
            self.res.append(self.words[cur_trie['$']])
            del cur_trie['$']

        if cur_idx is None:
            valid_indices = ((i, j) for i in range(len(board)) for j in range(len(board[0])))
        else:
            valid_indices = self._getNeighbors(board, cur_idx)

        for i, j in valid_indices:
            char = board[i][j]
            if char in cur_trie and (i, j) not in visited:
                visited.add((i, j))
                self._dfs(board, visited, (i, j), cur_trie[char])
                visited.remove((i, j))

    def _getNeighbors(self, board, cur_idx):
        r, c = cur_idx
        res = list()
        
        if r > 0:
            res.append((r - 1, c))
        if c > 0:
            res.append((r, c - 1))
        if r < len(board) - 1:
            res.append((r + 1, c))
        if c < len(board[0]) - 1:
            res.append((r, c + 1))

        return res
    
    def _computeTrie(self, words):
        trie = dict()
        for word_idx in range(len(words)):
            word = words[word_idx]
            tmp = trie
            for char in word:
                if char not in tmp:
                    tmp[char] = dict()
                tmp = tmp[char]
            tmp['$'] = word_idx
        return trie