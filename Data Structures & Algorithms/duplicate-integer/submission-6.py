class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {num: 0 for num in nums}
        for i in nums:
            mp[i] += 1
        
        for x,y in mp.items():
            if y > 1:
                return True
        return False