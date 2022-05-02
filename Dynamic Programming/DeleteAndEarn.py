"""
https://leetcode.com/problems/delete-and-earn/

You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.
"""

from collections import defaultdict


class Solution:
    ans = 0

    def deleteAndEarn(self, nums: List[int]) -> int:
        qw = defaultdict(int)

        for i in nums:
            qw[i] = qw[i] + 1

        qw = dict(sorted(qw.items(), key=lambda x: x[0], reverse=False))

        keys = list(qw)
        print(qw)

        qw1 = [0] * (len(keys) + 1)

        for i in range(len(keys)):
            if i == 0:
                qw1[1] = qw[keys[i]] * keys[i]
            else:
                if keys[i] - 1 in qw:
                    qw1[i + 1] = max(qw[keys[i]] * keys[i] + qw1[i - 1], qw1[i])
                else:
                    qw1[i + 1] = qw1[i] + qw[keys[i]] * keys[i]

        return qw1[-1]