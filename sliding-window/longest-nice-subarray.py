from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        i = 0  # Left pointer
        or_mask = 0  # Keeps track of OR value of current subarray
        max_len = 0  # Stores the max length

        for j in range(len(nums)):  # Right pointer expanding
            while (or_mask & nums[j]) != 0:  # If conflict, shrink window
                or_mask ^= nums[i]  # Remove nums[i] from OR mask
                i += 1  # Move left pointer

            or_mask |= nums[j]  # Include nums[j] in the OR mask
            max_len = max(max_len, j - i + 1)  # Update max length

        return max_len  # Return the maximum found




        