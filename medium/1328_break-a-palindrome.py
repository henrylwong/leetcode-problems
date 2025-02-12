class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""

        is_odd = len(palindrome) % 2
        mid = len(palindrome) // 2
        for idx in range(len(palindrome)):
            if palindrome[idx] == 'a' or (is_odd and idx == mid):
                continue
            else:
                palindrome = palindrome[:idx] + 'a' + palindrome[idx + 1:]
                return palindrome
        return palindrome[:-1] + 'b'