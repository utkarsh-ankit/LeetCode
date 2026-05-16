from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        # 1. Build gaps array
        gaps = [startTime[0]]
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])
        
        # 2. Sliding window over k+1 gaps
        window_sum = sum(gaps[:k+1])
        res = window_sum
        
        for i in range(k + 1, len(gaps)):
            window_sum += gaps[i] - gaps[i - (k+1)]
            res = max(res, window_sum)
        
        return res
