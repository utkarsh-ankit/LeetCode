from collections import Counter
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        res = 0
        for x, cnt in count.items():
            group_size = x + 1
            groups = math.ceil(cnt / group_size)
            res += groups * group_size
        return res
