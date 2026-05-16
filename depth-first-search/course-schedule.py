class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}
        degree={i:0 for i in range(numCourses)}

        for c,p in prerequisites:
            graph[p].append(c)
            degree[c]+=1
        
        queue=[node for node in degree if degree[node]==0]
        processed=0

        while queue:
            course=queue.pop()
            processed+=1

            for nei in graph[course]:
                degree[nei]-=1
                if degree[nei]==0:
                    queue.append(nei)
        
        return processed==numCourses