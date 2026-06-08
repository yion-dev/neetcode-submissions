class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            alphabets = [0] * 26

            for c in s:
                alphabets[ord(c) - ord('a')] += 1
                
            result[tuple(alphabets)].append(s)

        return list(result.values())
