class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        result = []
        nums.sort()

        for index, element in enumerate(nums):

            if element > 0:
                break
    
            if index > 0 and element == nums[index - 1]:
                continue

            start = index + 1
            end = len(nums) - 1

    
            while start < end:

                if nums[index] + nums[start] + nums[end] == 0:
                    result.append([nums[index], nums[start], nums[end]])

                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start - 1]:
                        start += 1

                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1

                    continue

                if nums[index] + nums[start] + nums[end] > 0:
                    end -= 1
                else:
                    start += 1
                
        return result

