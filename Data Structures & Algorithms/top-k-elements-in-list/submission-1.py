class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in nums:
            mp[i] = 1 + mp.get(i,0)
        
        heap = []
        for val in mp.keys():
            heapq.heappush(heap,(mp[val],val))
            if len(heap) > k:
                heapq.heappop(heap)

        out = []
        for i in range(k):
            out.append(heapq.heappop(heap)[1])
        return out