from collections import Counter

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = Counter(tuple(sorted(d)) for d in dominoes)
        return sum(f * (f - 1) // 2 for f in counts.values())
        