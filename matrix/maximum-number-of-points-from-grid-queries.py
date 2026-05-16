from typing import List
from heapq import heappush, heappop

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        from collections import deque

        n, m = len(grid), len(grid[0])
        k = len(queries)
        indexed_queries = sorted([(q, i) for i, q in enumerate(queries)])
        answer = [0] * k

        # Min-heap BFS
        heap = [(grid[0][0], 0, 0)]
        visited = [[False] * m for _ in range(n)]
        visited[0][0] = True

        # Count of reachable cells
        count = 0
        res = []

        # Sort queries so we can process cells in increasing order
        idx = 0  # index for queries
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while heap:
            val, x, y = heappop(heap)

            # Advance through queries while current cell is less than query value
            while idx < k and indexed_queries[idx][0] <= val:
                answer[indexed_queries[idx][1]] = count
                idx += 1

            count += 1

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heappush(heap, (grid[nx][ny], nx, ny))

        # Any remaining queries larger than all grid values
        while idx < k:
            answer[indexed_queries[idx][1]] = count
            idx += 1

        return answer
