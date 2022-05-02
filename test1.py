class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        ans = []
        for i in words:
            temp = words[i]

            if len(pattern) == len(temp):
                as= {}

                for i1 in range(len(temp)):
                    if temp[i1] in as





