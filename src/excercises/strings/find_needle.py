class Solution:
    """
    Find needle in haystack and return position in haystack of first occurence of needle
    If haystack is empty return 0
    If needle is not found return -1
    """
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        if n_len == 0:
            return 0
        for h_pos in range(h_len - n_len + 1):
            match = True
            for delta in range(n_len):
                if haystack[h_pos + delta] != needle[delta]:
                    match = False
                    break
            if match:
                return h_pos
        return -1
