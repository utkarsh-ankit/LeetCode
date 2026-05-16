from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        ans = -1
        for v, c in freq.items():
            if v == c and v > ans:
                ans = v
        return ans

        