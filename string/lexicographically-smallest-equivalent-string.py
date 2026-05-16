class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if ra < rb:
                parent[rb] = ra
            else:
                parent[ra] = rb
        for c1, c2 in zip(s1, s2):
            union(ord(c1) - 97, ord(c2) - 97)
        res = []
        for c in baseStr:
            r = find(ord(c) - 97)
            res.append(chr(r + 97))
        return "".join(res)
