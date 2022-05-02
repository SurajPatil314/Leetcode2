"""
https://leetcode.com/problems/3sum-smaller/

Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k
 < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
"""


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        i = 0
        j = 1
        k = 2

        if len(nums) < 3:
            return 0

        ans = 0

        nums = sorted(nums)

        while (i < len(nums) - 2):
            j = i + 1
            while (j < len(nums) - 1):
                k = j + 1
                while (k < len(nums)):
                    if (nums[i] + nums[j] + nums[k]) < target:
                        ans += 1
                        k += 1
                    else:
                        break

                j += 1
            i += 1

        return ans


