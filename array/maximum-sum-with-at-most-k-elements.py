class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        t=[]
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
            for j in range(limits[i]):
                heapq.heappush(t, -grid[i][j])

        summax=0
        while k>0 and t:
            summax+=-heapq.heappop(t)
            k-=1
        
        return summax




        