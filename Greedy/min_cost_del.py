"""
https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/


Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.
"""


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:

        i = 0
        costx = 0
        while (i < len(s) - 1):
            if s[i] != s[i + 1]:
                i += 1
            else:
                # print(costx)
                # print('pos',i)
                j = i + 1
                maxv = max(cost[i], cost[i + 1])
                minv = cost[i] + cost[i + 1]
                while (j < len(s) - 1):
                    if s[j] == s[j + 1]:
                        minv = minv + cost[j + 1]
                        if maxv < cost[j + 1]:
                            maxv = cost[j + 1]

                        j = j + 1
                    else:
                        break
                # print(maxv,minv)
                costx = costx + minv - maxv

                i = j + 1

        return costx


