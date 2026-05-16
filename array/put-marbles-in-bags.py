from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            # No cuts, so difference is zero
            return 0

        n = len(weights)
        pair_sums = [weights[i] + weights[i + 1] for i in range(n - 1)]

        pair_sums.sort()

        # Max score - min score based on k - 1 cuts
        max_score = sum(pair_sums[-(k - 1):])
        min_score = sum(pair_sums[:(k - 1)])

        return max_score - min_score
