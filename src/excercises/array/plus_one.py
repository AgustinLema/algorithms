from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            multiplier = 10 ** (len(digits) -  1 - i)
            num += digits[i] * multiplier

        num += 1
        digits_plus = []
        while num != 0:
            digits_plus.append(num % 10)
            num //= 10
        return digits_plus[::-1]


class Solution2:
    """
    Increment last digit, if it overflows (if it was 9) then incrase next element as well
    Otherwise break.
    Should be really careful to copy the array since I want to keep other values untouched
    To insert in first position use insert(pos, value)
    Complexity: 3n worst case (To copy array, to increase all digits and then to move them to insert a new char)
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        digits2 = digits[:]
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits2[i] = 0
            else:
                digits2[i] = digits[i] + 1
                break
        if digits2[0] == 0:
            digits2.insert(0, 1)
        return digits2


class Solution3:
    """
    Using negative index to loop over array from end to beginning
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        multiplier = 1
        for i in range(len(digits)):
            num += digits[-i - 1] * multiplier
            multiplier *= 10

        num += 1
        digits_plus = []
        while num != 0:
            digits_plus.append(num % 10)
            num //= 10
        return digits_plus[::-1]


class Solution4:
    """
    In place modification
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        if digits[0] == 0: # This check is not really needed.
            digits.insert(0, 1)
        return digits
