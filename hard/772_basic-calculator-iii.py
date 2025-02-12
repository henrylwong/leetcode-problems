#!/usr/bin/env python3

from collections import deque

'''
Basic Calculator III
--------------------
You are required to implement a basic calculator that evaluates simple expression strings. 
The expression string may contain open and closing parentheses, plus and minus signs, non-negative integers, multiplication and division operators, and empty spaces. 
For integer division, you should truncate towards zero. 
The expression is always valid and all intermediate results will be within the range of [-2147483648, 2147483647].

Here are some examples:
"1 + 1" should output: 2
" 6-4 / 2 " should output: 4
"2*(5+5*2)/3+(6/2+8)" should output: 21
"(2+6* 3+5- (3*14/7+2)*5)+3" should output: -12
'''

class Solution(object):
  '''
  Traverse the given expression from left to right and operate on each subexpr (in brackets) independently
  Immediately prioritize mul / div operations (via stack)
  Compute add / sub operations once a level is exhausted (via queue)
  '''
  def calculate(self, s):
    """
    :type s: str
    :rtype: int
    """
    # Mapping: char->op
    self.ops = {
      '+': Solution._add,
      '-': Solution._sub,
      '*': Solution._mul,
      '/': Solution._div
    }
    # Subexpression levels (by brackets); initialize level 0 stacks
    self.level = 0
    self.op_stack = [deque()]
    self.term_stack = [deque()]

    return self.calculate_subexpr(s)

  def calculate_subexpr(self, s):
    idx = 0
    while idx < len(s):
      skip_length = 1
      # Ignore whitespaces
      if s[idx] == ' ':
        idx += skip_length
        continue

      # Handle Ops
      if s[idx] in self.ops:
        self.op_stack[self.level].append(self.ops[s[idx]])
      # Handle Opening Brackets
      elif s[idx] == '(':
        self.term_stack.append(deque())
        self.op_stack.append(deque())
        self.level += 1 
      else:
        # Handle Closing Brackets
        if s[idx] == ')':
          # Add/Sub terms on same subexpr level
          self._calculate_addsub()
          # Append result to lower subexpr level
          self.term_stack[self.level - 1].append(self.term_stack[self.level][0])
          # Cleanup current subexpr level
          del self.term_stack[self.level]
          del self.op_stack[self.level]
          self.level -= 1
        # Handle terms
        else:
          term, skip_length = self.get_term(s, idx) 
          self.term_stack[self.level].append(term)
        
        # Mul/Div terms on same subexpr level (immediate priority)
        self._calculate_muldiv()
        
      idx += skip_length

    # Add/Sub remaining terms for default level
    self._calculate_addsub()

    assert(self.level == 0)
    return self.term_stack[self.level][0]

  def get_term(self, s, start_idx):
    idx = start_idx
    while idx < len(s) and s[idx].isdigit():
        idx += 1
    return int(s[start_idx:idx]), (idx - start_idx)
  
  def _calculate_muldiv(self):  
    if len(self.op_stack[self.level]) and (prev_op := self.op_stack[self.level][-1]) in [Solution._mul, Solution._div]: 
      second_term = self.term_stack[self.level].pop()
      self.term_stack[self.level][-1] = prev_op(self.term_stack[self.level][-1], second_term)
      self.op_stack[self.level].pop()

  def _calculate_addsub(self):
    for op in self.op_stack[self.level]:
      first_term = self.term_stack[self.level].popleft()
      self.term_stack[self.level][0] = op(first_term, self.term_stack[self.level][0])

  @staticmethod
  def _add(a, b):
    assert(isinstance(a, int) and isinstance(b, int))
    return a + b

  @staticmethod
  def _sub(a, b):
    assert(isinstance(a, int) and isinstance(b, int))
    return a - b
  
  @staticmethod
  def _mul(a, b):
    assert(isinstance(a, int) and isinstance(b, int))
    return a * b

  @staticmethod
  def _div(a, b):
    assert(isinstance(a, int) and isinstance(b, int))
    return int(a / b)

if __name__ == "__main__":
  cases = {
    # Basic Calculator III testcases
    "1 + 1": 2,
    " 6-4 / 2 ": 4,
    "2*(5+5*2)/3+(6/2+8)": 21, 
    "(2+6* 3+5- (3*14/7+2)*5)+3": -12,
    "(0-3)/4": 0,
    # Basic Calculator II testcases
    "3+2*2": 7,
    "3/2": 1,
    "3+5 / 2": 5,
    "1-1+1":1, 
    # Basic Calculator I testcases
    "1 + 1": 2,
    " 2-1 + 2 ": 3,
    "(1+(4+5+2)-3)+(6+8)": 23,
    "0": 0,
    # Additional testcases
    "(23 * 2) - 3 * (33 + 4 * 2 - 7)": -56,
    "7 * 8": 56
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