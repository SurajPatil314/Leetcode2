"""
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.


"""


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        topfreq = 0
        ans1 = []

        for i in range(len(dictionary)):

            qw1 = len(s)
            qw2 = len(dictionary[i])
            temp = dictionary[i]

            if qw2 <= qw1:
                if s == temp:
                    return temp
                i1 = 0
                j1 = 0

                while (i1 < qw1 and j1 < qw2):

                    if s[i1] == temp[j1]:
                        i1 += 1
                        j1 += 1
                    else:
                        i1 += 1

                if j1 == qw2:
                    if topfreq < qw2:
                        ans1 = []
                        ans1.append(temp)
                        topfreq = qw2
                    elif topfreq == qw2:
                        ans1.append(temp)

        if topfreq == 0:
            return ''
        else:
            if len(ans1) > 1:
                ans1 = sorted(ans1)
                return ans1[0]
            elif len(ans1) == 1:
                return ans1[0]
            else:
                return ''
