#!/usr/bin/env python3

DO_DEBUG = True

class Solution(object):
  def parseBoolExpr(self, expression):
    """
    :type expression: str
    :rtype: bool
    """
    self.func_mapping = {
      '&': self._parseAndExpr,
      '|': self._parseOrExpr,
      '!': self._parseNotExpr
    }
    res = self._evalExpr(expression)
    if res == 't':
      return True
    return False

  def _getSubExprs(expr):
    # return expr[2:-1].split(',')
    start_idx = 2
    cur_idx = 2
    num_parens = 0
    res = list()
    while cur_idx < len(expr) - 1:
      char = expr[cur_idx]
      if char == '(':
        num_parens += 1
      elif char == ')':
        num_parens -= 1
      elif char == ',' and num_parens == 0:
        res.append(expr[start_idx: cur_idx])
        start_idx = cur_idx + 1
      cur_idx += 1

    res.append(expr[start_idx: cur_idx])
    return res
  
  def _evalExpr(self, expr):
    if DO_DEBUG:
      print(expr)
    prefix = expr[0]
    if prefix in self.func_mapping:
      prefix = self.func_mapping[prefix](expr)
    return prefix    

  def _parseAndExpr(self, expr):
    assert(expr[0] == '&')
    subexprs = Solution._getSubExprs(expr)
    
    for subexpr in subexprs:
      res = self._evalExpr(subexpr)
      if res == 'f':
        return 'f'
      else:
        continue
        
    return 't'

  def _parseOrExpr(self, expr):
    assert(expr[0] == '|')
    subexprs = Solution._getSubExprs(expr)
    for subexpr in subexprs:
      res = self._evalExpr(subexpr)
      if res == 't':
        return 't'
      else:
        continue
        
    return 'f'

  def _parseNotExpr(self, expr):
    assert(expr[0] == '!')
    subexprs = Solution._getSubExprs(expr)
    assert(len(subexprs) == 1)

    res = self._evalExpr(subexprs[0])
    if res == 't':
      return 'f'
    return 't'

if __name__ == "__main__":
  # expression = "&(|(f))" # false
  # expression = "|(f,f,f,t)" # true
  expression = "!(&(f,t))" # true

  soln = Solution()
  res = soln.parseBoolExpr(expression)
  print(res)