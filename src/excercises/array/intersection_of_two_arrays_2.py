from typing import List


class Solution:
    """
    Find the intersection of two arrays.
    Input: Two arrays
    Output: Array with the intersection (elements shared).
    If there are multiple occurence of same element, return same amount.
    """
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) <= len(nums2):
            smaller, bigger = nums1, nums2
        else:
            smaller, bigger = nums2, nums1

        num_count={}
        for num in smaller:
            num_count[num] = num_count.get(num, 0) + 1

        inter = []
        for num in bigger:
            if num in num_count:
                inter.append(num)
                if num_count[num] < 2:
                    del num_count[num]
                else:
                    num_count[num] -= 1

        return inter


class Solution2:
    """
    Without extra memory
    Also better if arrays are already sorted
    """
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        pointer_1, pointer_2 = 0, 0
        inter = []

        while pointer_1 < len(nums1) and pointer_2 < len(nums2):
            if nums1[pointer_1] == nums2[pointer_2]:
                inter.append(nums1[pointer_1])
                pointer_1 += 1
                pointer_2 += 1
            elif nums1[pointer_1] < nums2[pointer_2]:
                pointer_1 += 1
            else:
                pointer_2 += 1
        return inter
