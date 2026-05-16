class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count=0
        adj={i:[] for i in range(n)}

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited=set()

        def dfs(t):
            visited.add(t)

            for nei in adj[t]:
                if nei not in visited:
                    dfs(nei)
            return
        
        for k in adj:
            if k not in visited:
                dfs(k)
                count+=1
        
        return count


















