"""
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous
subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such
 subarray, return 0 instead.
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        start = 0
        end = 0
        ans = sys.maxsize

        if len(nums) < 2:
            if len(nums) >= target:
                return 1
            else:
                return 0

        while (start <= end and end < len(nums)):
            if sum(nums[start:end + 1]) >= target:

                while (start <= end):
                    if sum(nums[start:end + 1]) >= target:
                        if ans >= end + 1 - start:
                            ans = end + 1 - start
                        start += 1
                    else:
                        break

                start = start + 1
                end = end

            else:
                end += 1

        if ans == sys.maxsize:
            return 0
        return ans


