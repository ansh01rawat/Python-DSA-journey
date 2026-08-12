from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        distance = [[-1] * len(mat[0]) for _ in range(len(mat))]
        queue = deque()
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    distance[row][col] = 0
                    queue.append((row, col))

        def bfs():
            while queue:
                level_size = len(queue)
                for _ in range(level_size):
                    row, col = queue.popleft()

                    for dr, dc in directions:
                        newRow = row + dr
                        newCol = col + dc

                        if (0 <= newRow < len(mat) and
                                0 <= newCol < len(mat[0]) and
                                distance[newRow][newCol] == -1):
                            distance[newRow][newCol] = distance[row][col] + 1
                            queue.append((newRow, newCol))

        bfs()
        return distance