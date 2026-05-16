from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        INF = 10**18
        # dist[i][j][p]: earliest time to arrive at (i,j) with next-move parity p
        dist = [[[INF] * 2 for _ in range(m)] for __ in range(n)]
        dist[0][0][0] = 0  # start at (0,0), next move costs 1 (p=0)
        
        # min-heap of (time, i, j, p)
        pq = [(0, 0, 0, 0)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while pq:
            t, i, j, p = heapq.heappop(pq)
            if t > dist[i][j][p]:
                continue
            # reached target
            if i == n-1 and j == m-1:
                return t
            
            move_cost = 1 if p == 0 else 2
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    # wait until the room is available
                    wait = max(0, moveTime[ni][nj] - t)
                    nt = t + wait + move_cost
                    np = 1 - p
                    if nt < dist[ni][nj][np]:
                        dist[ni][nj][np] = nt
                        heapq.heappush(pq, (nt, ni, nj, np))
        
        # problem guarantees reachability, but return -1 as a fallback
        return -1
