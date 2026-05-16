from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        curr_pairs = 0
        result = 0

        for right in range(len(nums)):
            # Add nums[right] to window
            curr_pairs += freq[nums[right]]
            freq[nums[right]] += 1

            # Shrink window from left while we have enough pairs
            while curr_pairs >= k:
                result += len(nums) - right  # all subarrays ending at right are valid
                curr_pairs -= freq[nums[left]] - 1  # remove left's contribution
                freq[nums[left]] -= 1
                left += 1

        return result
