import heapq
from typing import List

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)
        # 1. Sort by start lᵢ
        queries.sort(key=lambda x: x[0])

        available = []   # max-heap of ends  (store -r)
        used = []        # min-heap of ends

        j = 0            # pointer into queries
        applied = 0      # count of queries we actually use

        for i in range(n):
            # Add all queries that start at i
            while j < q and queries[j][0] == i:
                heapq.heappush(available, -queries[j][1])
                j += 1

            # Remove any used queries that no longer cover i
            while used and used[0] < i:
                heapq.heappop(used)

            # Ensure nums[i] decrements: need at least nums[i] active intervals
            remaining = nums[i] - len(used)
            while remaining > 0:
                if not available or -available[0] < i:
                    return -1
                # Take the query with farthest r
                r = -heapq.heappop(available)
                heapq.heappush(used, r)
                applied += 1
                remaining -= 1

        # Queries we didn’t apply = total − applied
        return q - applied
