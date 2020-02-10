from typing import List


class Solution:
    """
    Given a number return the inverse number by flipping characters
    Examples:
    123 -> 321
    120 -> 21
    -123 -> -321
    """
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        sum = 0
        sign = abs(x)//x
        x = abs(x)
        while x != 0:
            sum *= 10
            sum += x % 10
            x = x//10

        sum *= sign
        if sum >= pow(2, 31) or sum < pow(-2, 31):
            return 0

        return sum


class Solution2:
    """
    With strings
    """
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        reversed_string = str(abs(x))[::-1]
        reversed_num = int(reversed_string) * sign

        if pow(-2,31) <= reversed_num < pow(2,31):
            return reversed_num
        else:
            return 0
