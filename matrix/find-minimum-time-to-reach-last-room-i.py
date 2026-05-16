from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]  # (time, x, y)
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        while pq:
            time, x, y = heapq.heappop(pq)
            if time > dist[x][y]:
                continue
            if (x, y) == (n - 1, m - 1):
                return time

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    start_move = max(time, moveTime[nx][ny])
                    arrival   = start_move + 1
                    if arrival < dist[nx][ny]:
                        dist[nx][ny] = arrival
                        heapq.heappush(pq, (arrival, nx, ny))

        # problem guarantees reachability
        return -1
