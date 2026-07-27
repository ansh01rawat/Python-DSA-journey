class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        freq = {}
        l = 0
        longest = 0
        for r in range(len(nums)):
            freq[nums[r]] = freq.get(nums[r],0) + 1
            while len(freq) > 2:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            longest = max(longest,r-l+1)
        return longest 