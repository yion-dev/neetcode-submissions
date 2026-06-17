class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
     
        result = []
        nums.sort()

        for index in range(len(nums)):

            start = index + 1
            end = len(nums) - 1

            while start < end:

                if nums[index] + nums[start] + nums[end] == 0 and [nums[start], nums[end], nums[index]] not in result:
                    result.append([nums[start], nums[end], nums[index]])
    
                if nums[index] + nums[start] + nums[end] > 0:
                    end -= 1
                else:
                    start += 1
                
        
        return result
