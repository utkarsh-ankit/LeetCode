class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        def get_distances(start):
            dist = [-1] * n
            d = 0
            cur = start
            while cur != -1 and dist[cur] == -1:
                dist[cur] = d
                d += 1
                cur = edges[cur]
            return dist
        d1 = get_distances(node1)
        d2 = get_distances(node2)
        ans = -1
        best = float('inf')
        for i in range(n):
            if d1[i] != -1 and d2[i] != -1:
                m = max(d1[i], d2[i])
                if m < best:
                    best = m
                    ans = i
        return ans

        