class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        lengths = [1]
        for op in operations:
            lengths.append(lengths[-1]*2)
        
        def dfs(k, idx, char):
            if idx == 0:
                return char
            
            half = lengths[idx-1]
            op = operations[idx-1]
            
            if k <= half:
                return dfs(k, idx-1, char)
            else:
                if op == 0:
                    return dfs(k - half, idx-1, char)
                else:
                    shifted = chr(((ord(char) - ord('a') + 1) % 26) + ord('a'))
                    return dfs(k - half, idx-1, shifted)
        
        return dfs(k, len(operations), 'a')
