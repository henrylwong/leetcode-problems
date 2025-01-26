#!/usr/bin/env python3

class Solution:
  def exist(self, board: list[list[str]], word: str) -> bool: 
    visited = set()

    return self._dfs(board, None, None, -1, word, visited)
  
  def _dfs(self, board, r, c, idx, word, visited):
    if idx == len(word) - 1:
      return True
    
    visited.add((r, c))

    if r == None and c == None:
      neighbors = self._getStart(board, word)
    else:
      neighbors = self._getNeighbors(board, r, c)
    for neigh in neighbors:
      if neigh in visited:
        continue

      neigh_r, neigh_c = neigh
      if board[neigh_r][neigh_c] == word[idx + 1]:
        if self._dfs(board, neigh_r, neigh_c, idx + 1, word, visited):
          return True
    
    visited.remove((r, c))

    return False
  
  def _getStart(self, board, word):
    res = list()

    for r in range(len(board)):
      for c in range(len(board[0])):
        if board[r][c] == word[0]:
          res.append((r, c))

    return res     
    
  def _getNeighbors(self, board, r, c):
    res = list() 

    if r > 0:
      res.append((r - 1, c))
    if r < len(board) - 1:
      res.append((r + 1, c))
    if c > 0:
      res.append((r, c - 1))
    if c < len(board[0]) - 1:
      res.append((r, c + 1))

    return res