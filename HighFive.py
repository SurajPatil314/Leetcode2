"""
https://leetcode.com/problems/high-five/

Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a
 student with IDi, calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with
 IDj and their top five average. Sort result by IDj in increasing order.

A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer
 division.
"""


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        qw = defaultdict(list)
        ans = []

        for i in range(len(items)):
            qw[items[i][0]].append(items[i][1])

        for i, j in qw.items():
            j1 = sorted(j, reverse=True)
            j2 = int(sum(j1[0:5]) / 5)
            ans1 = []
            ans1.append(i)
            ans1.append(j2)
            ans.append(ans1)

        ans = sorted(ans, key=lambda x: x[0])

        return ans
