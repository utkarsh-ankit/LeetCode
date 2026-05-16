class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=list(blocks)
        t=float('inf')

        for i in range(len(l)-k+1):
            j=i+k
            t=min(t, l[i:j].count('W'))
        
        return t

            
        