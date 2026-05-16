from typing import List
from functools import lru_cache

class Solution:
    def minTravelTime(
        self,
        l: int,
        n: int,
        k: int,
        position: List[int],
        time: List[int],
    ) -> int:
        denavopelu = (l, n, k, position[:], time[:])

        @lru_cache(maxsize=None)
        def dfs(
            idx: int,          
            merges_left: int,
            prev_idx: int,    
            prev_time: int, 
            run_time: int      
        ) -> int:

            if idx == n - 1:
                if merges_left != 0:
                    return float("inf")         
                return (position[idx] - position[prev_idx]) * prev_time

            if merges_left < 0:
                return float("inf")            


            cost_remove = dfs(
                idx + 1,
                merges_left - 1,
                prev_idx,
                prev_time,
                run_time + time[idx],
            )


            seg_cost   = (position[idx] - position[prev_idx]) * prev_time
            cost_keep  = seg_cost + dfs(
                idx + 1,
                merges_left,
                idx,
                time[idx] + run_time,  
                0                      
            )

            return min(cost_remove, cost_keep)

        return dfs(1, k, 0, time[0], 0)
