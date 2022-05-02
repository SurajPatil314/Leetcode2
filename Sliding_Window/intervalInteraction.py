"""
https://leetcode.com/problems/interval-list-intersections/


You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
"""


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        ans = []
        i1 = 0
        i2 = 0
        firstf = 0
        lastf = 0
        firsts = 0
        lasts = 0

        if len(firstList) > 0 and len(secondList) > 0:
            firstf = firstList[0][0]
            lastf = firstList[0][1]
            firsts = secondList[0][0]
            lasts = secondList[0][1]

            while (i1 < len(firstList) and i2 < len(secondList)):
                # print(i1,i2)
                if firstf == firsts and lastf == lasts:
                    ans.append(firstList[i1])

                    if i1 + 1 < len(firstList):
                        firstf = firstList[i1 + 1][0]
                        lastf = firstList[i1 + 1][1]

                    if i2 + 1 < len(secondList):
                        firsts = secondList[i2 + 1][0]
                        lasts = secondList[i2 + 1][1]

                    i1 += 1
                    i2 += 1
                elif lasts < firstf:
                    # print('NA1')

                    if i2 + 1 < len(secondList):
                        firsts = secondList[i2 + 1][0]
                        lasts = secondList[i2 + 1][1]

                    i2 += 1
                elif lastf < firsts:
                    # print('NA2')

                    if i1 + 1 < len(firstList):
                        firstf = firstList[i1 + 1][0]
                        lastf = firstList[i1 + 1][1]

                    i1 += 1
                elif lastf > lasts:
                    # print('@@')
                    ans1 = []
                    ans1.append(max(firstf, firsts))
                    ans1.append(lasts)

                    if len(ans1) == 1:
                        ans1.append(ans[-1])

                    ans.append(ans1)
                    ans1 = []

                    if i2 + 1 < len(secondList):
                        firsts = secondList[i2 + 1][0]
                        lasts = secondList[i2 + 1][1]

                    i2 += 1

                elif lasts > lastf:
                    # print('##')

                    ans1 = []

                    ans1.append(max(firstf, firsts))
                    ans1.append(lastf)

                    ans.append(ans1)
                    ans1 = []

                    if i1 + 1 < len(firstList):
                        firstf = firstList[i1 + 1][0]
                        lastf = firstList[i1 + 1][1]

                    i1 += 1

                elif firstf > firsts:
                    ans1 = []

                    ans1.append(max(firsts, firstf))
                    ans1.append(lastf)

                    ans.append(ans1)

                    if i1 + 1 < len(firstList):
                        firstf = firstList[i1 + 1][0]
                        lastf = firstList[i1 + 1][1]

                    if i2 + 1 < len(secondList):
                        firsts = secondList[i2 + 1][0]
                        lasts = secondList[i2 + 1][1]

                    i1 += 1
                    i2 += 1



                elif firsts > firstf:
                    ans1 = []

                    ans1.append(max(firsts, firstf))
                    ans1.append(lastf)

                    ans.append(ans1)

                    if i1 + 1 < len(firstList):
                        firstf = firstList[i1 + 1][0]
                        lastf = firstList[i1 + 1][1]

                    if i2 + 1 < len(secondList):
                        firsts = secondList[i2 + 1][0]
                        lasts = secondList[i2 + 1][1]

                    i1 += 1
                    i2 += 1

        return ans






