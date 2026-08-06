def dfs(node,res,adj,vis):
    vis[node] = 1
    res.append(node)
    for x in adj[node]:
        if vis[x] == 0:
            dfs(x,res,adj,vis)


n = 8
adjacency_list = [[],[2,4],[1,3,6],[2],[1,5,7],[4,8],[2],[4,8],[5,7]]
visited = [0]*(n+1)
result = []
dfs(1,result,adjacency_list,visited)
print(result)