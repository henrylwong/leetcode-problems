class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
    res = ""
    carry = 0
    ord_0 = ord('0')
    num1_delta, num2_delta = max(0, len(num2) - len(num1)), max(0, len(num1) - len(num2))

    for idx in range(max(len(num1), len(num2)) - 1, -1, -1):
      a, b = 0, 0
      
      a_idx, b_idx = idx - num1_delta, idx - num2_delta
      if 0 <= a_idx < len(num1):
        a = ord(num1[a_idx]) - ord_0
      if 0 <= b_idx < len(num2):
        b = ord(num2[b_idx]) - ord_0
      summ = a + b + carry

      carry = 0
      if summ >= 10:
        carry = 1

      res = str(summ % 10) + res

    if carry:
        res = '1' + res
    return res