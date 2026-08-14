class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        a= defaultdict(list)
        for course, prere in prerequisites:
            a[course].append(prere)
            
        path=set()
        done=set()
            
        def dfs(n):
            if n in path:
                return False
            if n in done:
                return True
            
            path.add(n)
            
            for neigh in a[n]:
                if not dfs(neigh):
                    return False
            
            path.remove(n)
            done.add(n)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True