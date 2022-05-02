"""
https://leetcode.com/problems/min-cost-to-connect-all-points/

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
"""


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        li = []

        for i in range(len(points)):
            li.append(-1)

        qw = {}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                qw[str(str(i) + ',' + str(j))] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        qw1 = dict(sorted(qw.items(), key=lambda x: x[1]))

        count = 0

        ans = 0

        latest = 0

        keys = qw1.keys()

        keys1 = []
        keys1.extend(keys)

        set1 = defaultdict(list)

        def find_parent(point):
            nonlocal li
            if li[point] == -1:
                return point
            else:
                return find_parent(li[point])

        point1 = set()

        while (len(keys1) > 0):

            keys11 = keys1[0]
            keysplit = keys11.split(',')

            first = min(int(keysplit[0]), int(keysplit[1]))
            second = max(int(keysplit[0]), int(keysplit[1]))

            x1 = find_parent(first)
            x2 = find_parent(second)

            if x1 == x2:
                del keys1[0]
            else:

                ans = ans + int(qw1[keys11])
                li[x2] = x1
                del keys1[0]

            point1.add(first)
            point1.add(second)

        return ans
