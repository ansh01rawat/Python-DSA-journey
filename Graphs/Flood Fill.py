class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
        originalColor = image[sr][sc]
        if originalColor == color:
            return image
        def dfs(row,col):
            image[row][col] = color
            for dr,dc in directions:
                newRow = row + dr
                newCol = col + dc
                if (0 <= newRow < len(image) and
                    0 <= newCol < len(image[0]) and
                    image[newRow][newCol] == originalColor):
                        dfs(newRow,newCol)
        dfs(sr,sc)
        return image