class Solution:
    def maxTargetNodes(
        self,
        edges1: list[list[int]],
        edges2: list[list[int]],
        k: int
    ) -> list[int]:
        # Build adjacency lists
        def build(edges: list[list[int]]) -> list[list[int]]:
            g = [[] for _ in range(len(edges) + 1)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            return g

        # DFS to count nodes within distance d from u
        def dfs(graph: list[list[int]], u: int, parent: int, d: int) -> int:
            if d == 0:
                return 1
            total = 1  # count u itself
            for v in graph[u]:
                if v != parent:
                    total += dfs(graph, v, u, d - 1)
            return total

        g1 = build(edges1)
        g2 = build(edges2)

        # Precompute Tree 2's best reach within k-1 (if k>0)
        max2 = 0
        if k > 0:
            for v in range(len(edges2) + 1):
                max2 = max(max2, dfs(g2, v, -1, k - 1))

        # Compute result for each node in Tree 1
        result = []
        for u in range(len(edges1) + 1):
            cnt1 = dfs(g1, u, -1, k)
            result.append(cnt1 + max2)

        return result
