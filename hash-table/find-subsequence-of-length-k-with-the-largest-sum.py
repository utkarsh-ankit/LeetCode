from typing import List
import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Store (value, index) pairs
        largest_k = heapq.nlargest(k, enumerate(nums), key=lambda x: x[1])
        # Sort by original indices to maintain order
        largest_k.sort(key=lambda x: x[0])
        return [num for idx, num in largest_k]

        