class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxfreq = 0
        longest = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0)+1
            maxfreq = max(maxfreq,freq[s[r]])

            while (r - l + 1) - maxfreq > k:
                freq[s[l]] -= 1
                l += 1
            longest = max(longest,(r-l+1))
        return longest