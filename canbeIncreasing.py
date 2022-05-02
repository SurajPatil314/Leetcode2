"""
https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).
"""


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:

        count = 0
        high = 0
        i = 0
        if len(nums) < 3:
            return True
        while (i < len(nums) - 1):
            if count < 2:
                if nums[i] >= nums[i + 1]:
                    if i < len(nums) - 2:
                        if nums[i + 2] > nums[i]:
                            count += 1
                            i += 2
                        else:
                            if i == 0:
                                count += 1
                                i += 1
                            else:
                                if nums[i - 1] >= nums[i + 1]:
                                    return False
                                else:
                                    count += 1
                                    i += 1

                    else:
                        count += 1
                        i += 1
                else:
                    i += 1


            else:
                return False
##
        if count < 2:
            return True
        return False
