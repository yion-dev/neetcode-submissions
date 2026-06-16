class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
    
        while numbers[start] + numbers[end] != target:
            if numbers[end] + numbers[start] > target:
                end -= 1
            else:
                start += 1

        return [start + 1, end + 1]