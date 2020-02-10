from typing import List


class Solution:
    """
    Check if one word is an anagram of another
    Both are in lowercase
    Complexity: O(n + m)
    Space complexity: O(k) where k is number of unique chars in s
    """
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        for char in t:
            if char in char_count:
                char_count[char] -= 1
            else:
                return False
        return len([char for char, count in char_count.items() if count > 0]) == 0