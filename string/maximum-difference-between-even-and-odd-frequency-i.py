class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        h = [(count) for count in freq.values()]
        m=0
        n=float('inf')
        for i in h:
            if i%2!=0:
                m=max(i,m)
            else:
                n=min(i,n)
        return m-n

        








        