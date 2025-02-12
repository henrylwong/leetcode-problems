from collections import deque

class WordDictionary:

  def __init__(self):
    self.trie = dict()
    self.levels = dict()
    self.terminator = '$'

  def addWord(self, word: str) -> None:
    word += self.terminator
    cur_dict = self.trie
    for char in word:
      if char not in cur_dict:
        cur_dict[char] = dict()
      cur_dict = cur_dict[char]

  def search(self, word: str) -> bool:
    return self._dfs_search(word)

  def _bfs_search(self, word: str) -> bool:
    word += self.terminator
    queue = deque([self.trie])
    
    idx = 0
    while queue:
      for _ in range(len(queue)):
        trie = queue.popleft()
        if word[idx] == '.': # wildcard
          for char in trie.keys():
            queue.append(trie[char])
        elif word[idx] in trie:
          if idx == len(word) - 1:
            return True
          queue.append(trie[word[idx]])

      idx += 1
        
    return False
  
  def _dfs_search(self, word: str) -> bool:
    word += self.terminator
    stack = [(self.trie, 0)]
    
    while stack:
      trie, idx = stack.pop()
      if word[idx] == '.': # wildcard
        for char in trie.keys():
          stack.append((trie[char], idx + 1))
      elif word[idx] in trie:
        if idx == len(word) - 1:
          return True
        stack.append((trie[word[idx]], idx + 1))
        
    return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)