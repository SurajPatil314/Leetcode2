"""
https://leetcode.com/problems/palindromic-substrings/
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:

        ans = 0

        def ispalindrome(i, j):
            nonlocal ans, s
            # print(i,j)
            while (i >= 0 and j < len(s)):
                if s[i] == s[j]:
                    ans += 1
                    i = i - 1
                    j = j + 1
                else:
                    break
            # print(ans,'@@@')

        for i in range(len(s)):
            if i < len(s) - 1:
                ispalindrome(i, i)
                ispalindrome(i, i + 1)
            else:
                ispalindrome(i, i)

            # print('$$$')

        return ans

