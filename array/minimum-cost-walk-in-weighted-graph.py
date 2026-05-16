from collections import defaultdict
from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                rx, ry = ry, rx
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu = DSU(n)
        
        # 1) Union all edges
        for u,v,w in edges:
            dsu.union(u,v)
        
        # 2) Initialize componentAND for each root
        # Use a dict so we only store the root(s) that appear
        componentAND = {}
        for i in range(n):
            root = dsu.find(i)
            if root not in componentAND:
                componentAND[root] = ~0  # All bits set

        # 3) Compute AND of edge weights in each component
        for u,v,w in edges:
            r = dsu.find(u)  # same as find(v)
            componentAND[r] &= w  # update AND for that component

        # 4) Answer queries
        ans = []
        for s,t in query:
            if dsu.find(s) != dsu.find(t):
                ans.append(-1)
            else:
                ans.append(componentAND[dsu.find(s)])
        
        return ans
