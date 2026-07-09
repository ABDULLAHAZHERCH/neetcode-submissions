class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        bucket = [[]for i in range(len(nums)+1)]

        for i in nums:
            mp[i] = 1 + mp.get(i,0)
    
        for num,count in mp.items():
            bucket[count].append(num)

        out = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                out.append(num)
                if len(out) == k:
                    return out