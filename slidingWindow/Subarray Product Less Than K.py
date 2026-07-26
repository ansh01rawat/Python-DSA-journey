class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        total = 1
        answer = 0
        if k <= 1:
            return 0
        for r in range(len(nums)):
            total *= nums[r]
            while total >= k:
                total //= nums[l]
                l += 1
            answer += r - l + 1
        return answer
