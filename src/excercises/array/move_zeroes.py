from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Should receive a list of numbers including zeros
        The output should have all zeroes on the right and the rest of the numbers should keep order
        Do not return anything, modify nums in-place instead.
        """
        fixed_pos = 0
        for num in nums:
            if num != 0:
                nums[fixed_pos] = num
                fixed_pos += 1
        nums[fixed_pos:] = [0] * (len(nums) - fixed_pos)


class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        By swapping elements, there will never be a non zero character between
        the two pointers, so it is safe to keep swapping and in the end all zeroes will be there
        """
        fixed_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[fixed_pos], nums[i] = nums[i], nums[fixed_pos]
                fixed_pos += 1
