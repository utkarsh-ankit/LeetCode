class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #DFS
        if not grid:
            return 0

        rows=len(grid)
        cols=len(grid[0])
        isl=0

        def dfs(a,b):
            if a<0 or b<0 or a>=rows or b>=cols or grid[a][b]!="1":
                return
            
            grid[a][b]="0"

            dfs(a,b+1)
            dfs(a,b-1)
            dfs(a+1,b)
            dfs(a-1,b)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    dfs(i,j)
                    isl+=1

        return isl




        
        