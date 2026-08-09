class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]
        count = 0
        def dfs(row,col):
            grid[row][col] = "0"
            for dr, dc in directions:
                newRow = row + dr
                newCol = col + dc
                if (0 <= newRow < len(grid) and
                    0 <= newCol < len(grid[0]) and
                    grid[newRow][newCol] == "1"):

                    dfs(newRow,newCol)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row,col)
        return count