#!/usr/bin/env python3

import pdb

class Solution(object):
  def calculate(self, s):
    """
    :type s: str
    :rtype: int
    """
    s = ''.join(s.split()) # remove unnecessary whitespaces
    return self._calculate_subexpr(s)

  def _calculate_subexpr(self, s):
    if s.isdigit():
      return int(s)

    res = None
    op_stack = list()
    term_stack = list()
    idx = 0

    while idx < len(s):
      is_op, op = self.is_op(s, idx)
      if is_op:
        op_stack.append(op)
        idx += 1
      else:
        term, term_length = self.get_term(s[idx:])
        term_stack.append(self._calculate_subexpr(term))

        if len(term_stack) == 1 and len(op_stack) > 0 and op_stack[0] == Solution._sub:
          term_stack.append(op_stack.pop()(0, term_stack.pop()))

        if len(term_stack) >= 2:
          second_term = term_stack.pop()
          first_term = term_stack.pop()
          term_stack.append(op_stack.pop()(first_term, second_term))
        idx += term_length

    res = term_stack[-1] 
    return res

  def is_op(self, s, idx):
    if s[idx] == '+':
      return True, Solution._add
    elif s[idx] == '-':
      return True, Solution._sub
    return False, None
      
  def get_term(self, s):
    idx = 0
    res = None
    if s[idx].isdigit():
      while idx < len(s) and s[idx].isdigit():
        idx += 1
      res = s[:idx]
      return res, len(res)

    assert(s[0] == '(')
    bracket_cnt = 1
    idx = 1
    while bracket_cnt != 0:
      if s[idx] == '(':
        bracket_cnt += 1
      elif s[idx] == ')':
        bracket_cnt -= 1
      idx += 1
    res = s[1: idx - 1]
    return res, len(res) + 2

  @staticmethod
  def _add(a, b):
    return int(a) + int(b)

  @staticmethod
  def _sub(a, b):
    return int(a) - int(b)

if __name__ == "__main__":
  cases = {
    "1 + 1": 2,
    " 2-1 + 2 ": 3,
    "(1+(4+5+2)-3)+(6+8)": 23,
    "0": 0,
    "-(2 + 3)": -5,
    "-2 + 1": -1,
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