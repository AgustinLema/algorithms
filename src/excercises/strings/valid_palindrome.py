class Solution:
    """
    A word is palindrome if it can be read from end to start and be exactly the same then from start to end
    For this excercise we ignore any non alfanumeric character and ignore case
    By using two pointers the word should be the same checking opposite sides
    Complexity: O(n) with O(1) space
    """
    def isPalindrome(self, s: str) -> bool:
        s_idx, e_idx = 0, len(s) - 1
        while s_idx < e_idx:
            if not s[s_idx].isalnum():
                s_idx += 1
            elif not s[e_idx].isalnum():
                e_idx -= 1
            elif s[s_idx].lower() == s[e_idx].lower():
                s_idx += 1
                e_idx -= 1
            else:
                return False
        return True
