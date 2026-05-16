class Solution:
    def minCostClimbingStairs(self, cost):
        n=len(cost)
        memo={}

        def f(i):
            if i>=n:
                return 0
            
            if i in memo:
                return memo[i]
            memo[i]=cost[i]+min(f(i+1),f(i+2))
            return memo[i]

        return min(f(0), f(1))




        