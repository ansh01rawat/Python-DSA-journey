class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        result = []
        used = [False] * len(nums)

        def dfs():
            if len(permutation) == len(nums):
                result.append(permutation.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i]:
                    continue
                used[i] = True
                permutation.append(nums[i])
                dfs()
                permutation.pop()
                used[i] = False

        dfs()
        return result
