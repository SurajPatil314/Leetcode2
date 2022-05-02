"""
https://leetcode.com/problems/unique-paths/


A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        qw = [[1] * n] * m
        for i in range(len(qw)):
            for j in range(len(qw[i])):
                tempans = 0
                if i > 0:
                    tempans = tempans + qw[i - 1][j]
                if j > 0:
                    tempans = tempans + qw[i][j - 1]
                if tempans > 0:
                    qw[i][j] = tempans

        print(qw)
        return qw[m - 1][n - 1]
