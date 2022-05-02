"""
https://leetcode.com/problems/jump-game/submissions/


You are given an integer array nums. You are initially positioned at the array's first index, and each element in the
 array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def ejump(pos):
            result1 = False
            if pos == 0:
                return True

            found = -1
            for i in range(pos - 1, -1, -1):
                if i + nums[i] >= pos:
                    found = i
                    break

            if found == -1:
                return False
            else:
                result1 = ejump(found)
            if result1 == False:
                return False
            else:
                return True

        result = ejump(len(nums) - 1)

        return result