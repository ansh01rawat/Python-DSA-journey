from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        queue = deque()
        count = 0
        minutes = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row,col))
                if grid[row][col] == 1:
                    count += 1
        def bfs():
            nonlocal count,minutes
            while queue:
                level_size = len(queue)
                rotted = False
                for _ in range (level_size):
                    row, col = queue.popleft()
                    for dr,dc in directions:
                        newRow = row + dr
                        newCol = col + dc

                        if(0 <= newRow < len(grid) and
                           0 <= newCol < len(grid[0]) and
                           grid[newRow][newCol] == 1):

                           grid[newRow][newCol] = 2
                           count -= 1
                           queue.append((newRow,newCol))
                           rotted = True
                if rotted:
                    minutes += 1
        bfs()
        if count > 0:
            return -1
        return minutes