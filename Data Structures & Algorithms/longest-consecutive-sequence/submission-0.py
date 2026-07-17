class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = set(nums)
        longest = 0

        for num in mp:
            if (num - 1) not in mp:
                length = 1
                while (num + length) in mp:
                    length += 1
                longest = max(length,longest)
        return longest