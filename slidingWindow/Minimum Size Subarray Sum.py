class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        l = 0
        answer = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                answer = min(answer, r - l + 1)
                total -= nums[l]
                l += 1
        if answer == float("inf"):
            return 0
        return answer