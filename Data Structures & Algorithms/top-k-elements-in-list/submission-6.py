class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        heap = []
        for element, key in frequency.items():
            heapq.heappush(heap, [key, element])

        while len(heap) > k:
            heapq.heappop(heap)

        result = []
        while len(heap) != 0:
            _, element = heapq.heappop(heap)
            result.append(element)

        return result
