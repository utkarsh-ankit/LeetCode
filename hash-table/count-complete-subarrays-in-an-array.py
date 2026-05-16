from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums):
        n = len(nums)
        totalDistinct = len(set(nums))
        count = 0
        freq = defaultdict(int)
        left = 0

        for right in range(n):
            freq[nums[right]] += 1
            
            # Try to shrink window from the left while it still contains all distinct elements
            while len(freq) == totalDistinct:
                count += n - right  # All subarrays from left to right, right+1, ..., n-1 are valid
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return count
