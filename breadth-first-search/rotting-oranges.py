#multi-source BFS
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        time,fresh=0,0
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])

        while q and fresh>0:
            for i in range(len(q)):
                a,b=q.popleft()
                for dr, dc in directions:
                    row,col=dr+a, dc+b
                    if (row<0 or row==len(grid) or col<0 or col==len(grid[0]) or grid[row][col]!=1):
                        continue
                    grid[row][col]=2
                    q.append([row, col])
                    fresh-=1
            time+=1
        
        return time if fresh==0 else -1

#In the real process, a fresh orange rots at the minimum distance to any rotten source, because it can be reached by whichever source is closer.