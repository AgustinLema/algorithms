class Solution:
    """
    The input is a non-empty list where all elements have two copies except for one
    Return the only element that has only one occurrence
    """
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = set()
        for num in nums:
            if num in seen_once:
                seen_once.remove(num)
            else:
                seen_once.add(num)
        return seen_once.pop()