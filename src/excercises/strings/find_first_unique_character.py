from typing import List


class Solution:
    """
    Return first index of a character that is not repeated in the string
    Complexity: O(n)
    """
    def firstUniqChar(self, s: str) -> int:
        num_count = {}
        for i in range(len(s)):
            num_count[s[i]] = num_count.get(s[i], 0) + 1
        unique_nums = [num for num, count in num_count.items() if count == 1]
        for i in range(len(s)):
            if s[i] in unique_nums:
                return i
        return -1


class Solution2:
    """
    Smaller constant by checking count while going over array
    """
    def firstUniqChar(self, s: str) -> int:
        num_count = {}
        for i in range(len(s)):
            num_count[s[i]] = num_count.get(s[i], 0) + 1
        for i in range(len(s)):
            if num_count[s[i]] == 1:
                return i
        return -1
