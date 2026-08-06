class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*(n)
        count = 0
        def dfs(city,matrix,visited):
            visited[city] = True
            for neighbour in range(len(matrix)):
                if matrix[city][neighbour] == 1 and not visited[neighbour]:
                    dfs(neighbour,matrix,visited)
        for i in range(0,n):
            if not visited[i]:
                count += 1
                dfs(i,isConnected,visited)
        return count