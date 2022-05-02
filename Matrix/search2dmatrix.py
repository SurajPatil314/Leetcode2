"""
https://leetcode.com/problems/search-a-2d-matrix-ii/

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        found = False
        if len(matrix) == 0:
            return found
        lr = len(matrix[0])
        lc = len(matrix)

        # print(lr,lc)
        def dfs(i, j, down, rev):
            nonlocal found, lr, lc, matrix, target
            # print(i,j)
            val = False
            if i >= lc or j >= lr:
                return False
            if down == 1:
                if rev == 0:
                    if matrix[i][j] == target:
                        print('%%%%1')
                        return True
                    else:
                        if i + 1 < lc:
                            if matrix[i + 1][j] <= target:
                                val = dfs(i + 1, j, 1, 0)
                            else:
                                val = dfs(i, j + 1, 1, 1)
                        else:
                            val = dfs(i, j + 1, 1, 1)

                else:
                    if matrix[i][j] == target:
                        print('%%%%2')
                        return True
                    else:
                        if j + 1 < lr:
                            if matrix[i][j + 1] <= target:
                                val = dfs(i, j + 1, 1, 1)
                            else:
                                return False
                        else:
                            return False
            else:
                if rev == 0:
                    if matrix[i][j] == target:
                        print('%%%%3')
                        return True
                    else:
                        if j + 1 < lr:
                            if matrix[i][j + 1] <= target:
                                val = dfs(i, j + 1, 0, 0)
                            else:
                                val = dfs(i + 1, j, 0, 1)
                        else:
                            val = dfs(i + 1, j, 0, 1)

                else:
                    if matrix[i][j] == target:
                        print('%%%%4')
                        return True
                    else:
                        if i + 1 < lc:
                            if matrix[i + 1][j] <= target:
                                val = dfs(i + 1, j, 0, 1)
                            else:
                                return False
                        else:
                            return False

            return val

        ans1 = dfs(0, 0, 1, 0)
        print('**')
        ans2 = dfs(0, 0, 0, 0)

        print(ans1, ans2)

        return ans1 or ans2
