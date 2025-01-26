#!/usr/bin/env python3

class Solution:
  modulo = (10 ** 9) + 7
  knight_mapping = {0:[4, 6],
                    1:[6, 8],
                    2:[7, 9],
                    3:[4, 8],
                    4:[0, 3, 9],
                    5:[],
                    6:[0, 1, 7],
                    7:[2, 6],
                    8:[1, 3],
                    9:[2, 4]}
  
  def knightDialer(self, n: int) -> int:
    # init state counts
    state_counts = dict()
    for i in range(10):
      state_counts[i] = 1 

    # iterate through states 1 -> n, updating state counts
    for i in range(2, n + 1):
      new_state_counts = dict()
      for state, count in state_counts.items():
        next_states = self.knight_mapping[state]

        for next_state in next_states:
          if next_state not in new_state_counts:
            new_state_counts[next_state] = count
          else:
            new_state_counts[next_state] += count

      state_counts = new_state_counts
    return sum(state_counts.values()) % self.modulo

if __name__ == "__main__":
  n = 3131

  soln = Solution()
  res = soln.knightDialer(n)
  print(res)