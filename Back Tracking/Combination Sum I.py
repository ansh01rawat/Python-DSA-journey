class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        result = []

        def dfs(i, value):
            if value == target:
                result.append(subset.copy())
                return
            if value > target or i == len(candidates):
                return
            subset.append(candidates[i])
            dfs(i, value + candidates[i])
            subset.pop()
            dfs(i + 1, value)

        dfs(0, 0)
        return result
