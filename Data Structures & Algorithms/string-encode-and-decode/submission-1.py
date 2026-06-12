class Solution:

    def encode(self, strs: list[str]) -> str:
        result = ""
        for s in strs: 
            result += (str(len(s)))
            result += "#"
            result += s
        return result

    def decode(self, s: str) -> list[str]:
        
        decoded = []
        startPointer = 0

        while startPointer < len(s):
            endPointer = startPointer

            while s[endPointer] != "#":
                endPointer += 1

            length = int(s[startPointer:endPointer])
            startPointer = endPointer + 1
            endPointer = startPointer + length

            decoded.append(s[startPointer:endPointer])
            startPointer = endPointer

        return decoded

