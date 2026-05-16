from collections import defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        def dfs(node):
            if node in path:
                return float("inf")  # cycle detected
            if node in visit:
                return 0  # already computed

            visit.add(node)
            path.add(node)

            colorIndex = ord(colors[node]) - ord('a')
            count[node][colorIndex] = 1

            for nei in adj[node]:
                if dfs(nei) == float("inf"):
                    return float("inf")
                for c in range(26):
                    count[node][c] = max(count[node][c], count[nei][c] + (1 if c == colorIndex else 0))

            path.remove(node)
            return max(count[node])

        n = len(colors)
        res = 0
        visit, path = set(), set()
        count = [[0] * 26 for _ in range(n)]

        for i in range(n):
            if i not in visit:
                val = dfs(i)
                if val == float("inf"):
                    return -1
                res = max(res, val)

        return res
