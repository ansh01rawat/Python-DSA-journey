class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        need = {}
        for ch in p:
            need[ch] = need.get(ch, 0) + 1
        window = {}
        l = 0

        if len(p) > len(s):
            return []
        for r in range(len(p)):
            window[s[r]] = window.get(s[r], 0) + 1
        r = len(p)

        if need == window:
            answer.append(l)
        while r < len(s):
            window[s[l]] -= 1
            if window[s[l]] == 0:
                del window[s[l]]
            l += 1
            window[s[r]] = window.get(s[r], 0) + 1
            r += 1
            if need == window:
                answer.append(l)

        return answer