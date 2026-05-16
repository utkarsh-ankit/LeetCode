class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s)%k!=0:
            d=len(s)%k
            s=s+fill*(k-d)
        a=[]
        for i in range(0,len(s),k):
            a.append(s[i:i+k])
        return a