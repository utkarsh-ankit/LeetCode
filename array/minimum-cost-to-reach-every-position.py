class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n=len(cost)
        t=[cost[0]]*n
        
        for i in range(n):
            t[i]=cost[i]

        for i in range(n):
            for j in range(i+1, n):
                t[j]=min(t[j], t[i])

        return t
        