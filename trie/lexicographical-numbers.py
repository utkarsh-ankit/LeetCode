from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result: List[int] = []
        
        def dfs(x: int) -> None:
            if x > n:
                return
            result.append(x)
            for i in range(10):
                nxt = x * 10 + i
                if nxt > n:
                    break
                dfs(nxt)
        
        for start in range(1, 10):
            if start > n:
                break
            dfs(start)
        
        return result

        