class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            hashset = set(nums)
            longest = 0
            current = 0
            
            for num in nums:
                if num - 1 not in hashset:
                    current = 1
                    index = 1
                    while num + index in hashset:
                        current += 1 
                        index += 1
                
                longest = max(longest, current)

            return longest
