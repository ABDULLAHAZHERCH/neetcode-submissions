class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smp = {si: 0 for si in sorted(s)}
        tmp = {ti: 0 for ti in sorted(t)}
        for i in s:
            smp[i] += 1
        for j in t:
            tmp[j] += 1
        if smp == tmp:
            return True
        return False   