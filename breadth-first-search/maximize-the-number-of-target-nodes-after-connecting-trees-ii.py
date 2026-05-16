from typing import List
import sys
sys.setrecursionlimit(10**7)

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def build_graph(edges: List[List[int]]) -> List[List[int]]:
            n = len(edges) + 1
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            return g

        def dfs(u: int, parent: int, is_even: bool, g: List[List[int]], parity: List[bool]) -> int:
            parity[u] = is_even
            cnt = 1 if is_even else 0
            for v in g[u]:
                if v == parent:
                    continue
                cnt += dfs(v, u, not is_even, g, parity)
            return cnt

        # Build adjacency
        g1, g2 = build_graph(edges1), build_graph(edges2)
        n1, n2 = len(g1), len(g2)

        # Color tree1 and tree2, count even‐level nodes
        parity1 = [False] * n1
        parity2 = [False] * n2
        even1 = dfs(0, -1, True,  g1, parity1)
        even2 = dfs(0, -1, True,  g2, parity2)

        odd1 = n1 - even1
        odd2 = n2 - even2
        best2 = max(even2, odd2)

        # For each i in tree1: take its own best + best2
        return [
            (even1 if parity1[i] else odd1) + best2
            for i in range(n1)
        ]
