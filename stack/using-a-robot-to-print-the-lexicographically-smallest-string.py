class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        # Build the suffix-min array
        suffix_min = [''] * n
        suffix_min[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(s[i], suffix_min[i + 1])
        
        stack = []
        result = []
        
        for i, ch in enumerate(s):
            stack.append(ch)
            # Determine the smallest character remaining in s after index i
            next_min = suffix_min[i + 1] if i + 1 < n else '{'  # '{' is lexicographically larger than 'z'
            
            # Pop from stack whenever its top is <= the smallest remaining char
            while stack and stack[-1] <= next_min:
                result.append(stack.pop())
        
        return "".join(result)
