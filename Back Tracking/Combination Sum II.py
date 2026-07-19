class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        result = []
        candidates.sort()
        def dfs(i,value):
            if value == target:
                result.append(subset.copy())
                return
            if value > target or i == len(candidates):
                return
            subset.append(candidates[i])
            dfs(i + 1,value + candidates[i])
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            subset.pop()
            dfs(i + 1,value)
        dfs(0,0)
        return result

