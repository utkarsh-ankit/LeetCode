class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        l=[]
        for i in range(1, int(n**0.5)+1):
            if n%i==0:
                l.append(i)
                if i != n//i:
                    l.append(n//i)
        l.sort()

        return l[k - 1] if k <= len(l) else -1

