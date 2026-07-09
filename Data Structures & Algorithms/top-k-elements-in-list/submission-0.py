class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {num:0 for num in nums}
        for i in nums:
            mp[i] += 1
        
        arr = []
        for val,key in mp.items():
            arr.append([key,val])
        arr.sort()

        out = []
        while len(out) < k:
            out.append(arr.pop()[1])
        return out