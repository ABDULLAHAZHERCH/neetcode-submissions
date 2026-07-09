class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for w in strs:
            alpha = [0] * 26
            for c in w:
                alpha[ord(c)-ord('a')] += 1
            mp[tuple(alpha)].append(w)
        return list(mp.values())
            