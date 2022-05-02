"""
https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ans = []
        ans2 = []
        for i in range(numRows):
            if i == 0:
                ans1 = [1]
                ans.append(ans1)

            elif i == 1:
                ans1 = [1, 1]
                ans.append(ans1)
            else:
                ans2 = ans[-1]
                ans1 = []
                temp = 0
                for i in range(len(ans2)):

                    if i == 0:
                        ans1.append(ans2[0])
                        temp = ans2[0]

                    elif i == len(ans2) - 1:
                        ans1.append(temp + ans2[i])
                        ans1.append(1)

                    else:
                        ans1.append(temp + ans2[i])
                        temp = ans2[i]

                ans.append(ans1)

        return ans




