class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t): return False
        countS, countT = [0] * 26, [0] * 26
        for i,c in enumerate(s):
            countS[ord(c) - ord("a")] += 1
            countT[ord(t[i]) - ord("a")] += 1

        if countS == countT:
            return True

        return False
