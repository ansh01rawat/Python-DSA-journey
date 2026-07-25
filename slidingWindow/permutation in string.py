class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1
        window = {}
        l = 0

        if len(s1) > len(s2):
            return False
        for r in range(len(s1)):
            window[s2[r]] = window.get(s2[r], 0) + 1
        r = len(s1)

        if need == window:
            return True
        while r < len(s2):
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1
            window[s2[r]] = window.get(s2[r], 0) + 1
            r += 1
            if need == window:
                return True

        return False