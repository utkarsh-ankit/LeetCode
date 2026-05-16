from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        l={i:[] for i in range(numCourses)}

        for a, b in prerequisites:
            l[b].append(a)

        
        deg={node:0 for node in l}

        for node in l:
            for nei in l[node]:
                deg[nei] += 1

        queue=deque([a for a in deg if deg[a]==0])
        ts=[]

        while queue:
            jnode=queue.popleft()
            ts.append(jnode)

            for nei in l[jnode]:
                deg[nei]-=1
                if deg[nei]==0:
                    queue.append(nei)

        return ts if len(ts) == numCourses else []
        


        