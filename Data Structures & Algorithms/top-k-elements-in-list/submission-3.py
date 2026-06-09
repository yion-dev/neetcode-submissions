class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = 1 + frequency.get(num , 0)
        heap = []
        for element,count in frequency.items():
            heapq.heappush(heap, [count, element])
        while len(heap) > k:
            heapq.heappop(heap)
        result = []
        for _ in range(len(heap)):
            _, item = heapq.heappop(heap)
            result.append(item)
        return result

