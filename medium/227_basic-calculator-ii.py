#!/usr/bin/env python3

from collections import deque

class Solution(object):
  

  def calculate(self, s):
    """
    :type s: str
    :rtype: int
    """
    self.ops = {
      '+': Solution._add,
      '-': Solution._sub,
      '*': Solution._mul,
      '/': Solution._div
    }

    s = ''.join(s.split()) # remove unnecessary whitespaces
    return self.calculate_subexpr(s)

  def calculate_subexpr(self, s):
    if s.isdigit():
      return int(s)

    res = None
    idx = 0
    stack = deque()
    while idx < len(s):
      if s[idx] in self.ops:
        stack.append(s[idx])
        idx += 1
      else:
        term, term_length = self.get_term(s[idx:])
        term = self.calculate_subexpr(term)

        if len(stack) >= 2  and stack[-1] in ['*', '/']:
          op = self.ops[stack.pop()]
          stack.append(op(stack.pop(), term)) 
        else:
          stack.append(term)

        idx += term_length

    while len(stack) > 1:
      first_term = stack.popleft()
      op = self.ops[stack.popleft()]
      second_term = stack.popleft()
      stack.appendleft(op(first_term, second_term))

    res = stack[0] 
    return res

  def get_term(self, s):
    idx = 0
    if s[0].isdigit():
      while idx < len(s) and s[idx].isdigit():
        idx += 1
      res = s[:idx]
      return res, len(res)

  @staticmethod
  def _add(a, b):
    return a + b

  @staticmethod
  def _sub(a, b):
    return a - b
  
  @staticmethod
  def _mul(a, b):
    return a * b

  @staticmethod
  def _div(a, b):
    return a // b

if __name__ == "__main__":
  cases = {
    "3+2*2": 7,
    "3/2": 1,
    "3+5 / 2": 5,
    "1-1+1":1, 
  }

  soln = Solution()
  for case in cases:
    print(f"Running case: {case}")
    res = soln.calculate(case)
    print(f"\tResult: {res}")
    if res == cases[case]:
        print(f"\t\033[92m\tStatus: PASS\033[0m")  
    else:
        print(f"\t\033[91m\tStatus: FAIL\033[0m")