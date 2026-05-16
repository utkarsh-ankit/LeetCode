from collections import defaultdict, deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = [False] * n
        
        # Step 1: Build graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs(start):
            q = deque([start])
            visited[start] = True
            nodes = [start]
            edge_count = 0
            
            while q:
                u = q.popleft()
                for v in graph[u]:
                    edge_count += 1
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
                        nodes.append(v)
            return nodes, edge_count // 2  # undirected: counted twice
        
        complete_components = 0
        
        for i in range(n):
            if not visited[i]:
                nodes, edge_count = bfs(i)
                v = len(nodes)
                expected_edges = v * (v - 1) // 2
                if edge_count == expected_edges:
                    complete_components += 1
        
        return complete_components
