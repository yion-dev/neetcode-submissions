class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)

        heap = []
        for element, index in frequency.items():
            heapq.heappush(heap, (-index, element))
        
        result = []
        for _ in range(k):
            _, number = heapq.heappop(heap)
            result.append(number)

        return result


