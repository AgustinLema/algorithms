from typings import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array with numbers, return the position of the two numbers that sum the target value
        Complexity: O(n^2)
        """
        for i in range(len(nums)):
            rest = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == rest:
                    return [i, j]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Read all numbers into a map first, then check the map for complements
        Complexity: O(2n)
        """
        num_pos = {}
        for i in range(len(nums)):
            num_pos[nums[i]] = i

        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in num_pos and num_pos[rest] != i:
                return [i, num_pos[rest]]


class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Write complement into map while numbers are being read
        Look if complement is there and return both values ordered
        Complexity: O(n)
        """
        compl_pos = {}       
        for i in range(len(nums)):
            if nums[i] in compl_pos:
                return [compl_pos[nums[i]], i]
            else:
                compl_pos[target - nums[i]] = i
