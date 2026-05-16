class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #BFS
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        visit=set()
        isl=0
        max_area=0

        def bfs(a,b):
            q=collections.deque()
            visit.add((a,b))
            q.append((a,b))
            area=1
            directions=[[1,0], [-1,0], [0,1], [0,-1]]
            while q:
                row, col=q.popleft()
                for dr, dc in directions:
                    a,b=row+dr, col+dc
                    if (a in range(rows) and b in range(cols) and grid[a][b]==1 and (a,b) not in visit):
                        q.append((a,b))
                        visit.add((a,b))
                        area+=1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    current=bfs(r,c)
                    max_area=max(max_area, current)
        return max_area