class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        n = len(startTime)
        # 1) Build gaps
        gaps = [startTime[0]] + [startTime[i] - endTime[i-1] for i in range(1, n)] + [eventTime - endTime[-1]]
        
        # 2) Build prefix and suffix maximums
        maxLeft = [0] * (n+1)
        maxRight = [0] * (n+1)
        
        maxLeft[0] = gaps[0]
        for i in range(1, n+1):
            maxLeft[i] = max(maxLeft[i-1], gaps[i])
        
        maxRight[n] = gaps[n]
        for i in range(n-1, -1, -1):
            maxRight[i] = max(maxRight[i+1], gaps[i])
        
        # 3) Evaluate best free time by possibly moving one meeting
        res = 0
        for i in range(n):
            dur = endTime[i] - startTime[i]
            adj = gaps[i] + gaps[i+1]
            largest_gap_elsewhere = 0
            if i > 0:
                largest_gap_elsewhere = max(largest_gap_elsewhere, maxLeft[i-1])
            if i+2 <= n:
                largest_gap_elsewhere = max(largest_gap_elsewhere, maxRight[i+2])
            
            candidate = adj + (dur if dur <= largest_gap_elsewhere else 0)
            res = max(res, candidate)
        
        return res
