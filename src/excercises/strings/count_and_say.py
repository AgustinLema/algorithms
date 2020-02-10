class Solution:
    """
    Write the nth call of count and say
    Count and say is a sequence starting from 1
    Then you read the count of the number and the number itself, so next value is 11
    And repeat:
    21 (Two 1s)
    1211 (One 2 and One 1)
    111221
    """
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            s = self._get_next(s)
        return s

    def _get_next(self, s):
        previous = s[0]
        count = 0
        new_s = []
        for c in s:
            if c == previous:
                count += 1
            else:
                new_s.extend([str(count), str(previous)])
                previous = c
                count = 1
        new_s.extend([str(count), str(previous)])
        return "".join(new_s)