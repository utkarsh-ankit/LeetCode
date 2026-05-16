from bisect import bisect_right

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        starts = [event[0] for event in events]

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, k_left):
            if i == n or k_left == 0:
                return 0
            # Option 1: skip event i
            res = dp(i+1, k_left)
            # Option 2: attend event i
            next_i = bisect_right(starts, events[i][1])
            res = max(res, events[i][2] + dp(next_i, k_left-1))
            return res

        return dp(0, k)
